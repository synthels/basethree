import hmac

from flask import Flask, session, request
from functools import wraps


class FlaskCsrf(Flask):
  """
  simple csrf protection
  """
  def csrf(self, f):
    @wraps(f)
    def protect(*args, **kwargs):
      token = request.cookies.get("XSRF-TOKEN")
      if token is None:
        hmac_digest = hmac.new(session["XSRF-TOKEN"], self.secret_key).digest()
        if not hmac.compare_digest(signature, hmac_digest):
          return "csrf", 400
        else:
          return f(*args, **kwargs)
      return "csrf", 400

    return protect
