import flask
from config import Config

app = flask.Flask(__name__)
app.config.from_object(Config)


@app.errorhandler(404)
def render_not_found(error):
    return flask.render_template("error-page.html",
                                 text_error="Ничего не нашлось! Вот неудача, отправляйтесь на главную!",
                                 error_code="404")


@app.errorhandler(500)
def render_server_error(error):
    return flask.render_template("error-page.html",
                                 text_error="Что-то не так, но мы все починим",
                                 error_code="500")


@app.route("/")
def render_index():
    return flask.render_template('index.html')


# @app.errorhandler(404)
# def page_not_found(e):
#     return flask.render_template('error-page.html'), 404


if __name__ == "__main__":
    app.run()
