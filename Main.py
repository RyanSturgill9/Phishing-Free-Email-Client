import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_message")
def get_message():
    return "Hello from the server!"

if __name__ == "__main__":
    app.run(debug=True)