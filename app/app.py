from flask import Flask, render_template
import db
import json
import datetime as dt

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/get_user/<username>")
def get_user(username):
    return json.dumps(db.get_user(username))

@app.route("/add_time/<ident>")
def add_time(ident):
    time = dt.datetime.now().isoformat()
    return json.dumps(db.new_person(ident, time))

@app.route("/add_data/<username>,<time>")
def add_data(username, time):
    time = dt.datetime.now().isoformat()
    return json.dumps(db.update_times(username, time))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)