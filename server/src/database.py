import psycopg2
from psycopg2 import pool
from psycopg2 import extras

from psycopg2.extensions import AsIs


class ConnectionTup:
  def __init__(self, cursor, connection):
    self.cursor = cursor
    self.connection = connection


class Credentials:
  def __init__(self, min_conn, max_conn, database, host, user, password, port):
    self.min_conn = min_conn
    self.max_conn = max_conn
    self.database = database
    self.host = host
    self.user = user
    self.password = password
    self.port = port


class Database:
  pool = None

  @classmethod
  def __init__(cls, c):
    try:
      if cls.pool is None:
        cls.pool = psycopg2.pool.SimpleConnectionPool(
            c.min_conn,
            c.max_conn,
            database=c.database,
            host=c.host,
            user=c.user,
            password=c.password,
            port=c.port,
        )
    except psycopg2.OperationalError as e:
      print(f"couldn't connect to database: {e}")
      exit()

  @classmethod
  def init_database(cls, sub, c, name, table):
    """
    Initialise database sub by creating a table
    called name, from key-value pairs in table.
    """
    if sub._instance is not None:
      return sub._instance
    sub._instance = sub.__new__(sub)
    try:
      cls.__init__(c)
      if not cls.table_exists(name):
        print(f"init: {sub.__name__}")
        cls.execute(
            "CREATE TABLE %s (%s)", (
                AsIs(name),
                AsIs(',\n'.join([f'{key} {t}' for key, t in table.items()]))
            )
        )
    except (psycopg2.OperationalError, psycopg2.ProgrammingError):
      print(f"error: couldn't init {sub.__name__}")
      exit()

  @classmethod
  def connection(cls):
    c = cls.pool.getconn()
    c.autocommit = True
    return ConnectionTup(c.cursor(), c)

  @classmethod
  def close(cls, conn):
    cls.pool.putconn(conn.connection)

  @classmethod
  def execute(cls, query, p=()):
    conn = cls.connection()
    with conn.cursor as c:
      try:
        c.execute(query, p)
      except (psycopg2.OperationalError, psycopg2.ProgrammingError):
        raise
      finally:
        cls.close(conn)

  @classmethod
  def fetch(cls, query, p=(), rows=0):
    conn = cls.connection()
    with conn.cursor as c:
      try:
        c.execute(query, p)
        if rows == 1:
          return c.fetchone()
        return c.fetchall() if (rows == 0) else c.fetchmany(size=rows)
      except (psycopg2.OperationalError, psycopg2.ProgrammingError):
        raise
      finally:
        cls.close(conn)

  @classmethod
  def table_exists(cls, table):
    return cls.fetch(
        f"""
      SELECT EXISTS (
        SELECT FROM information_schema.tables 
        WHERE  table_schema = 'public'
        AND    table_name   = '{table}'
      );
      """,
        (),
        1,
    )[0]
