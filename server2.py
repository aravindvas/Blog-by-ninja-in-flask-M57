from flask import Flask, render_template
import random
import datetime
import requests

apia = "https://api.agify.io/?"
apig = "https://api.genderize.io/?"

app = Flask(__name__)

@app.route('/')
def hello():
    r = random.randint(1,10)
    y = datetime.datetime.now().year
    return render_template("index2.html", n=r, yr=y)

@app.route('/guess/<name>')
def hell(name):
    y = datetime.datetime.now().year
    gurl = f'{apig}name={name}'
    grsp = requests.get(url=gurl)
    gend = grsp.json()["gender"]
    aurl = f'{apia}name={name}'
    arsp = requests.get(url=aurl)
    age = arsp.json()["age"]
    return render_template("guess.html", yr=y, name=name, gen=gend, ag=age)

@app.route('/blog/<no>')
def blg(no):
    print(no)
    y = datetime.datetime.now().year
    burl = "https://api.npoint.io/ec3c64c26e1ee4e3dc69"
    brsp = requests.get(url=burl)
    allp = brsp.json()
    return render_template("blog.html", yr=y, pst=allp)



if __name__ == "__main__" :
    app.run(debug=True)