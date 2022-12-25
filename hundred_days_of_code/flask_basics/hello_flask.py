from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_flask():
    return "Hello Flask!!</b?"


@app.route("/bye")
def bye_flask():
    return "Bye Bye!!"
