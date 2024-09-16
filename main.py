import flask

app = flask.Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/<path>')
def home():
    # return "Hello, World!"
    return flask.render_template('index.html', title='Home', message='Hello, World!')

if __name__ == "__main__":
    app.run()
