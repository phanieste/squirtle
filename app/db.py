from firebase import firebase
from firebase_token_generator import create_token
import os

FIREBASE_URL = 'https://resplendent-torch-6836.firebaseio.com'
FIREBASE_SECRET = os.environ.get('FIREBASE_SECRET', '')

# create an auth token
auth_payload = {'uid': '1', 'auth_data': 'users'}
token = create_token(FIREBASE_SECRET, auth_payload)

firebase = firebase.FirebaseApplication(FIREBASE_URL)

def get_user(username):
    username = '"' + username + '"'
    result = firebase.get('/users', None, 
                        params={'print': 'pretty', 
                                'auth': token,
                                'orderBy': '"$key"', 
                                'equalTo': username})
    return result