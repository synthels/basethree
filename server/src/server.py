import os

from dotenv import load_dotenv

from flask import Flask
from flask_cors import CORS, cross_origin

from csrf import FlaskCsrf
from database import Credentials
from user import UsersDatabase

app = FlaskCsrf(__name__)


def main():
  CORS(app, supports_credentials=True)

  if os.path.isfile(".config"):
    load_dotenv(".config")
  else:
    print("please create a '.config' file. (see the README for details)")
    exit()

  app.secret_key = os.getenv("SESSION_SECRET").encode("utf-8")

  UsersDatabase.instance(
      Credentials(
          os.getenv("PG_MIN_CONNECTIONS"),
          os.getenv("PG_MAX_CONNECTIONS"),
          os.getenv("PG_DATABASE"),
          os.getenv("PG_HOST"),
          os.getenv("PG_USER"),
          os.getenv("PG_PASSWORD"),
          os.getenv("PG_PORT"),
      )
  )


if __name__ == "server":
  main()

import auth
