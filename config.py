import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SOME SECRET KEY 01'
    SQL_ALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqllite:///' + os.path.join(base_dir, 'app.db')