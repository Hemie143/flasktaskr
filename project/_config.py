import os


basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

DATABASE = 'flasktaskr.db'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'myprecious'

DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH