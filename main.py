from flask import Flask, render_template
import datetime
import requests


app = Flask(__name__)


@app.route('/')
def home():
    year = datetime.datetime.now().year
    return render_template('index.html', year=year)


@app.route('/<name>')
def hello(name):
    gen = requests.get(f"https://api.genderize.io/?name={name}")
    gender = gen.json()["gender"]
    ag = requests.get(f"https://api.agify.io/?name={name}")
    age = ag.json()["age"]
    # print(gender, age)
    return render_template('home.html', name=name, gender=gender, age=age)


@app.route('/blog')
def blog():
    posts = requests.get("https://api.npoint.io/3e4817776942ecfb2b89")
    posts = posts.json()
    return render_template("blog.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)


