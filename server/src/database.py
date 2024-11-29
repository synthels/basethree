import psycopg2
from psycopg2 import pool
from psycopg2 import extras


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
  @classmethod
  def __init__(self, c):
    try:
      self.pool = psycopg2.pool.SimpleConnectionPool(
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
