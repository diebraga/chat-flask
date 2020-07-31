import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Main page with structure"""
    return "to send message use USERNAME / MESSAGE"

@app.route('/<username>')
def user(username):
    return "Hi " + username

@app.route("/<username>/<message>")
def send_message(username, message):
    return "{0}: {1}".format(username, message)


if __name__ =="__main__":
    app.run(debug=True)
