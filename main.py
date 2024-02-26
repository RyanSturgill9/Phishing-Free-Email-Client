
import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    token_path = 'token.pickle'

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            print(f"Authorization URL: {flow.authorization_url()}")
            creds = flow.run_local_server(port=0, authorization_prompt_message='')

        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

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
