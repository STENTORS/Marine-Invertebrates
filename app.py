from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
import API
app = Flask(__name__)

@app.route("/")
def home():
    data = API.get_marine_invertebrates()
    return render_template("index.html", data=data)


@app.route("/collection")
def collection():
    data = API.get_marine_invertebrates()
    return render_template("collection.html", data=data)
