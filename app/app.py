from flask import Flask, render_template, request
import db
import json
import datetime as dt
import requests
import time
app = Flask(__name__)

@app.route("/")
def main():
<<<<<<< HEAD

=======
>>>>>>> 9c1885c5c556ec52f9adcc26dfb000b9841ed01b
    return render_template('homepage.html')

@app.route("/get_user/<username>")
def get_user(username):
    return json.dumps(db.get_user(username))

@app.route("/add_time/<ident>", methods=['GET', 'POST'])
def add_time(ident):
    if method.request == 'POST':
        time = dt.datetime.now()
        return time

@app.route("/add_data/<ident>", methods=['GET', 'POST'])
def add_data(ident):
    if method.request == 'POST':
        time = dt.datetime.now()
        return str(db.update_times(ident, time))

@app.route('/currentTime', methods=['GET', 'POST'])
def currentTime():
	if request.method == 'POST':
         return self.client_address[0]
	else:
		return 'wrong'

@app.route("/get_time")
def get_time():
    return db.get_time()

@app.route("/line_count")
def line_count():
    return str(db.count_line())


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)