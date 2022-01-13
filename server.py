from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    burl = "https://api.npoint.io/ec3c64c26e1ee4e3dc69"
    brsp = requests.get(url=burl)
    allp = brsp.json()
    return render_template("index.html", pst=allp)

@app.route('/blog/<index>')
def blg(index):
    print(index)
    burl = "https://api.npoint.io/ec3c64c26e1ee4e3dc69"
    brsp = requests.get(url=burl)
    allp = brsp.json()
    return render_template("post.html", pst=allp, indx=int(index))



if __name__ == "__main__" :
    app.run(debug=True)