import os

from flask import Flask, render_template

app = Flask(__name__)


def get_secret():
    return "\n".join(str(os.environ.get(f"line_{i}")) for i in range(1, 5))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/yes")
def reveal_secret():
    secret_value = get_secret()
    return render_template("secret.html", secret=secret_value)


@app.route("/no")
def hide_secret():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
