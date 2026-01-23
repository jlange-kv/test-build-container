import os

from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    secret_link = url_for("secret")
    return f"<h1>Hello!</h1><p><a href='{secret_link}'>Watch the secret here!</a>"


@app.route("/secret")
def secret():
    return str(os.environ.get("my_secret"))


app.run()
