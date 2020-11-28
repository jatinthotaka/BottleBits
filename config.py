import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://jatinsql:Sankara1@@localhost:3306/mb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

