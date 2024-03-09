import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'users.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "secret_key"

    # Затирание куки #
    # PERMANENT_SESSION_LIFETIME = timedelta(minutes=1)
