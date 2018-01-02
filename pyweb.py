from flask import Flask
from flask import render_template
from flask import redirect

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


@app.route("/file/<path:path>")
def file_redirect(path):
    return redirect("/static/file/{}".format(path), code=302)


@app.route("/blog")
def blog_redirect():
    return redirect("/", code=302)


@app.route("/blog/<path:n>")
def blog_path_redirect(n):
    return redirect("/", code=302)


if __name__ == '__main__':
    # app.run("0.0.0.0")
    app.run()
