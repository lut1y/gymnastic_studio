import flask_migrate
import flask_sqlalchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = flask_sqlalchemy.SQLAlchemy()
migrate = flask_migrate.Migrate()
admin = Admin()


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


admin.add_view(ModelView(UserModel, db.session))
