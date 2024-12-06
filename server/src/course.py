import os
import re
from datetime import datetime
from pathlib import Path

import psycopg2

from database import Database
from statuscodes import *

import json
import yaml


def snake(s):
  return '_'.join(
      re.sub(
          '([A-Z][a-z]+)', r' \1',
          re.sub('([A-Z]+)', r' \1', s.replace('-', ' '))
      ).split()
  ).lower()


class Course:
  def __init__(self, name, data):
    self.name = name
    self.data = data


class CoursesDatabase(Database):
  _instance = None
  pool = None

  @classmethod
  def instance(cls, c=None):
    return super().init_database(
        cls, c, "courses", {
            "course": "JSONB",
            "last_update": "TIMESTAMP",
        }
    )

  @classmethod
  def get(cls, cid):
    try:
      c = cls.fetch(
          """SELECT course FROM courses WHERE course->>'id' = %s
        """, (cid, ), 1
      )
      if c is None:
        return None
      return Course(c[0]["title"], c[0])
    except (psycopg2.OperationalError, psycopg2.ProgrammingError) as e:
      raise HttpInternalServerError

  @classmethod
  def add(cls, data):
    try:
      cls.execute(
          """INSERT INTO courses (course, last_update)
        VALUES (%s, %s)
        """, (json.dumps(data), datetime.now())
      )
    except (psycopg2.OperationalError, psycopg2.ProgrammingError) as e:
      raise HttpInternalServerError

  @classmethod
  def load(cls, d):
    """
    Loads all courses from directory d into
    the database.
    """
    try:
      if not os.path.isdir(d):
        print(f"error: directory {d} doesn't exist.")

      with os.scandir(d) as it:
        try:
          for course in it:
            f = open(Path(d) / course.name / "course.yml")
            data = yaml.safe_load(f.read())
            cls.add(data.update({"id": snake(data["title"])}))
        except FileNotFoundError:
          print(f"error: course {course.name} doesn't have a course.yml file.")
    except HttpInternalServerError:
      raise
