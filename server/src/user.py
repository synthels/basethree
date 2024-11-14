import bcrypt
import psycopg2

import re

from database import Database
from statuscodes import *


class User:
  def __init__(self, name, email, password, data):
    self.name = name
    self.email = email
    self.password = password
    self.data = data


class UsersDatabase(Database):
  _instance = None
  pool = None

  @classmethod
  def instance(cls, c=None):
    if cls._instance is not None:
      return cls._instance
    cls._instance = cls.__new__(cls)
    try:
      super(UsersDatabase, cls).__init__(c)
      if not cls.table_exists("users"):
        print("created users table")
        cls.execute(
            """CREATE TABLE users (
            username      VARCHAR(32),
            email         VARCHAR(256),
            password      VARCHAR(256),
            session_token VARCHAR(256),
            data          JSONB
          );
          """
        )
    except (psycopg2.OperationalError, psycopg2.ProgrammingError):
      print("couldn't create users table.")
      exit()

  @classmethod
  def get(cls, name):
    try:
      u = cls.fetch(
          """
      SELECT * FROM users WHERE username = %s
      """,
          (name, ),
          1,
      )
      if u is None:
        return None
      return User(u[0], u[1], u[2], u[3])
    except (psycopg2.OperationalError, psycopg2.ProgrammingError) as e:
      raise HttpInternalServerError

  @classmethod
  def get_session(cls, token):
    try:
      u = cls.fetch(
          """
      SELECT * FROM users WHERE session_token = %s
      """,
          (token, ),
          1,
      )
      if u is None:
        return None
      return User(u[0], u[1], u[2], u[3])
    except (psycopg2.OperationalError, psycopg2.ProgrammingError) as e:
      raise HttpInternalServerError

  @classmethod
  def add(cls, user):
    try:
      if cls.get(user.name) is not None:
        raise HttpForbidden("user already exists")
      salt = bcrypt.gensalt()
      pwd_hashed = bcrypt.hashpw(user.password.encode("utf-8"),
                                 salt).decode("utf-8")
      cls.execute(
          """
        INSERT INTO users (username, email, password)
        VALUES (%s, %s, %s)
        """,
          (user.name, user.email, pwd_hashed),
      )
    except (psycopg2.OperationalError, psycopg2.ProgrammingError) as e:
      raise HttpInternalServerError
    except HttpStatus:
      raise

  @classmethod
  def compare(cls, u1, u2):
    """
    compare two users (not commutative!)
    """
    return bcrypt.checkpw(
        u1["password"].encode("utf-8"), u2.password.encode("utf-8")
    )


def creds_good(u):
  """
  check whether user credentials
  are sensible.
  """
  # TODO: maybe compile this
  if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", u["email"]):
    return False
  return (
      (len(u["username"]) <= 32) and (len(u["password"]) <= 256) and
      (len(u["email"]) <= 256)
  )
