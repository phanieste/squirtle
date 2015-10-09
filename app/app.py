from flask import Flask, render_template
import db
import json

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


@app.route("/get_user/<username>")
def get_user(username):
    return json.dumps(db.get_user(username))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)