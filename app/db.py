from firebase import firebase
from firebase_token_generator import create_token
from dateutil.parser import parse

import datetime as dt
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
    result = firebase.post('/line', { 'ident': ident, 
                'timestamp': time.isoformat() }, 
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

    total_time = time - parse(data['timestamp'])
    new_entry = {'ident': ident, 'timeIn': data['timestamp'], 'timeOut': time, 
                'total': str(total_time)}
    firebase.post('/data', new_entry, connection=None, 
                    params={'print': 'pretty', 'auth': token})
    firebase.delete('/line', key, connection=None, 
                    params={'print': 'pretty', 'auth': token})
    return str(total_time)

# get last completed wait time
def get_time():
    # ident = "hji3724"
    # result = firebase.get('/line', None, connection=None,
    #         params={'print': 'pretty', 
    #             'auth': token,
    #             'orderBy': '"ident"'})
                # 'equalTo': str('"' + ident + '"')})
    result = firebase.get('/data', None, connection=None,
            params={'print': 'pretty', 
                'auth': token,
                'orderBy': '"timeOut"',
                'limitToLast': '1'})
    total_time = result[result.keys()[0]]['total']
    return total_time