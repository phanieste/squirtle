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
    result = firebase.get('/users', username, {'print': 'pretty', 
                                                'auth': token })                                
    return result

# add a person in line
def new_person(ident, time):
    result = firebase.post('/line', { 'ident': ident, 'timestamp': time }, 
                connection=None, params={'print': 'pretty', 'auth': token})
    return result

# person has left line, add wait time to database
def update_times(ident, time):
    result = firebase.get('/line', None, connection=None,
            params={'print': 'pretty', 
                'auth': token,
                'orderBy': '"ident"',
                'equalTo': str('"' + ident + '"')})
    key = result.keys()[0]
    data = result[key]
    total_time = time - data['timestamp']
    new_entry = {'name': name, 'timeIn': data['timestamp'], 'timeOut': time, 
                'total': total_time}
    firebase.post('/data', new_entry, conection=None, 
                    params={'print': 'pretty', 'auth': token})
    firebase.delete('/line', key)

