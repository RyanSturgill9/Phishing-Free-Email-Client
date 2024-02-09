import flask
from flask import Flask, render_template
## need to add:
## Google oauth2 (from google.oauth2.credentials import Credentials)
## Google oauth library (from google_auth_oauthlib.flow imort InstalledAppFlow)
## Google requests (from google.auth.transport.requests import Requests)





app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_message")
def get_message():
    return "Hello from the server!"

if __name__ == "__main__":
    app.run(debug=True)