import flask
from flask import Flask, render_template
## need to add:
## Google oauth2 (from google.oauth2.credentials import Credentials)
## Google oauth library (from google_auth_oauthlib.flow imort InstalledAppFlow)
## Google requests (from google.auth.transport.requests import Requests)

import os
import base64
import google.auth
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None

    # The file token.json stores the user's access and refresh tokens.
    token_path = 'client_secret_96534092037-hedc84l2q4hnfs5ihmg06cntm7nea9op.apps.googleusercontent.com.json'

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return creds

def list_messages(service, user_id='me', query=''):
    try:
        response = service.users().messages().list(userId=user_id, q=query).execute()
        messages = response.get('messages', [])
        return messages
    except Exception as e:
        print(f"An error occurred: {e}")

def get_message(service, user_id='me', msg_id=''):
    try:
        message = service.users().messages().get(userId=user_id, id=msg_id).execute()
        return message
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Authenticate Gmail API
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)

    # Example: List the latest 5 messages
    messages = list_messages(service, query='in:inbox', user_id='me')
    for message in messages[:5]:
        msg_id = message['id']
        msg = get_message(service, msg_id=msg_id)
        print(f"Subject: {msg['subject']}")
        print(f"Snippet: {msg['snippet']}")
        print("---------------")

if __name__ == '__main__':
    main()




#app = Flask(__name__)

#@app.route("/")
#def index():
#    return render_template("index.html")

#@app.route("/get_message")
#def get_message():
#    return "Hello from the client"

#if __name__ == "__main__":
#    app.run(debug=True)
