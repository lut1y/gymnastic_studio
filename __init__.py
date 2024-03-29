import flask


def create_app(config_file='config.py'):
    app = flask.Flask(__name__)

    app.config.from_pyfile(config_file)

    # db.init_app(app)

    # login_manager.init_app(app)

    # login_manager.login_view = 'auth.login'

    # @login_manager.user_loader
    # def load_user(user_id):
    #     retun User.query.get(user_id)

    # app.register_blueprint(main)
    # app.register_blueprint(auth)

    # app.cli.add_command(create_tables)

    return app
