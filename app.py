from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request 
import API
app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    error = request.args.get("error") 
    return render_template("index.html", error=error) 


@app.route("/collection")
def collection():
    try:
        data = API.get_marine_invertebrates()
        return render_template("collection.html", data=data)
    except:
        return redirect(url_for("home", error="Error fetching data from the API."))


@app.route("/game")
def game():
    return render_template("ocean_game.html")

@app.route("/accessability")
def accessability():
    return render_template("accessability.html")