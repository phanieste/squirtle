from flask import Flask, render_template, request
import db
import json
import datetime as dt
import requests
import time
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('homepage.html', 
        last_time=db.get_time(),
        line_length=db.count_line())

@app.route("/got_in_line", methods=['POST'])
def got_in_line():
    if request.method == 'POST':
        ip = request.remote_addr
        time = dt.datetime.now()
        return str(db.new_person(ip, time))

@app.route("/out_of_line", methods=['POST'])
def out_of_line():
    if request.method == 'POST':
        ip = request.remote_addr
        time = dt.datetime.now()
        return str(db.update_times(ip, time))


@app.route("/get_time", methods=['GET', 'POST'])
def get_time():
    return db.get_time()


@app.route("/line_count", methods=['GET', 'POST'])
def line_count():
    print(request.remote_addr)
    return str(db.count_line())
    

@app.route('/currentTime', methods=['GET', 'POST'])
def currentTime():
	if request.method == 'POST':
         return self.client_address[0]
	else:
		return 'wrong'


@app.route("/systemInformation", methods= ['POST'])
def getInfo():
    print('something')
    if request.method == 'POST':
        time  = db.get_time()
        peopleInLine = db.count_line()
        systemInfo = {'time' : time, "People in Line": peopleInLine}
        return json.dumps(systemInfo)


# test endpoints for DB interaction
@app.route("/test_get_user/<username>")
def test_get_user(username):
    return json.dumps(db.get_user(username))


@app.route("/test_add_time/<ident>", methods=['GET', 'POST'])
def test_add_time(ident):
    if method.request == 'POST':
        time = dt.datetime.now()
        return time


@app.route("/test_add_data/<ident>", methods=['GET', 'POST'])
def test_add_data(ident):
    if method.request == 'POST':
        time = dt.datetime.now()
        return str(db.update_times(ident, time))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)