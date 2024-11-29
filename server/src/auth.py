from flask import request, session, make_response

from user import UsersDatabase, creds_good
from statuscodes import HttpStatus
from server import app
import json
import hmac
import secrets

from user import User, UsersDatabase

users = UsersDatabase.instance()


@app.route("/auth", methods=["POST"])
def auth():
  session.permanent = True
  token = None
  if "session_token" in session:
    token = session["session_token"]
  if token is not None:
    u = users.get_session(token)
    if u is not None:
      return "", 200

  try:
    u1 = json.loads(request.data)
    if tuple_any_empty(u1, ("username", "password")):
      return "one or more fields is missing", 400
    u2 = users.get(u1["username"])
    if u2 is None:
      return "user doesn't exist", 404
    if not users.compare(u1, u2):
      return "incorrect password", 403
  except HttpStatus:
    raise

  # give the user a csrf token
  token = secrets.token_hex(32)
  session["session_token"] = token
  session["xsrf_token"] = hmac.new(
      app.secret_key, token.encode("utf-8"), "sha256"
  ).hexdigest()

  resp = make_response("", 200)
  resp.set_cookie("XSRF-TOKEN", session["xsrf_token"], samesite="None")
  return resp


@app.route("/signup", methods=["POST"])
def signup():
  user = json.loads(request.data)
  if tuple_any_empty(user, ("username", "email", "password")):
    return "one or more fields is missing", 400
  if not creds_good(user):
    return "bad credentials", 400
  try:
    users.add(User(user["username"], user["email"], user["password"], None))
  except HttpStatus as e:
    return str(e), e.statuscode()
  return "", 200


def tuple_any_empty(d, tup):
  """
  check whether any entries of d
  with keys in tup are empty or missing.
  """
  for k in tup:
    if (k not in d.keys()) or d[k] == "" or d[k].isspace():
      return True
  return False
