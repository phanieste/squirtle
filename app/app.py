from flask import Flask, render_template
import db
import json
import datetime as dt

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('homepage.html')

@app.route("/get_user/<username>")
def get_user(username):
    return json.dumps(db.get_user(username))

@app.route("/add_time/<ident>")
def add_time(ident):
    time = dt.datetime.now()
    return json.dumps(db.new_person(ident, time))

@app.route("/add_data/<ident>")
def add_data(ident):
    time = dt.datetime.now()
    return str(db.update_times(ident, time))

@app.route("/get_time")
def get_time():
    return db.get_time()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)