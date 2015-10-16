from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')
@app.route("/")
def main():
    user = {'nickname': 'John'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        },
        {
        	'author': {'nickname' : 'Braxton'},
        	'body' : 'Is that a world tour or your girls tour?'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    