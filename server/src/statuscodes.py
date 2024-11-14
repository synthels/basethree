# some http status codes we need


class HttpStatus(Exception):
  def __init__(self, msg=""):
    self.msg = msg

  def __str__(self):
    return self.msg

  def statuscode(self):
    pass


class HttpForbidden(HttpStatus):
  def statuscode(self):
    return 403


class HttpInternalServerError(HttpStatus):
  def statuscode(self):
    return 500
