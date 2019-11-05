# db_create.py

from project import db
from project.models import Task, User
from datetime import date

db.create_all()

# db.session.add(User("admin", "ad@min.com", "admin", "admin"))
# db.session.add(Task("Finish this tutorial", date(2016,  10, 3), 10, date(2020, 10, 10), 1, 1))
# db.session.add(Task("Finish Real Python", date(2016,  10, 3), 10, date(2021, 10, 10), 1, 1))

db.session.commit()
