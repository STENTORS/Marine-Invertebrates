from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
import API
app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/collection")
def collection():
    data = API.get_marine_invertebrates()
    return render_template("collection.html", data=data)

@app.route("/game")
def game():
    return render_template("ocean_game.html")

@app.route("/accessability")
def accessability():
    return render_template("accessability.html")