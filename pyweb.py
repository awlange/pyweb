from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/robots.txt")
def robots():
    return app.send_static_file("robots.txt")


@app.route("/humans.txt")
def humans():
    return app.send_static_file("humans.txt")


@app.route("/nav")
def nav():
    return "", 204


if __name__ == '__main__':
    app.run()
