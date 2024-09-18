import flask
from markupsafe import escape

app = flask.Flask(__name__)

# import logging
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/hello/<name>')
def hello(name):
    print(flask.request.path)
    # query = flask.request.args.get('name')
    # print(f'Hello {escape(name)}')
    return flask.render_template('greeting.html', title='Home', message='Hello, World!', name=name, path=flask.request.path)

if __name__ == "__main__":
    app.run()
