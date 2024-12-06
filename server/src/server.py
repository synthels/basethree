import os

from dotenv import load_dotenv

from flask import Flask
from flask_cors import CORS, cross_origin

from csrf import FlaskCsrf
from database import Credentials
from user import UsersDatabase
from course import CoursesDatabase

app = FlaskCsrf(__name__)


def main():
  CORS(app, supports_credentials=True)

  if os.path.isfile(".config"):
    load_dotenv(".config")
  else:
    print("please create a '.config' file. (see the README for details)")
    exit()

  creds = Credentials(
      os.getenv("PG_MIN_CONNECTIONS"),
      os.getenv("PG_MAX_CONNECTIONS"),
      os.getenv("PG_DATABASE"),
      os.getenv("PG_HOST"),
      os.getenv("PG_USER"),
      os.getenv("PG_PASSWORD"),
      os.getenv("PG_PORT"),
  )

  app.secret_key = os.getenv("SESSION_SECRET").encode("utf-8")

  UsersDatabase.instance(creds)
  CoursesDatabase.instance(creds)

  CoursesDatabase.load(os.getenv("COURSES"))


if __name__ == "server":
  main()

import auth
