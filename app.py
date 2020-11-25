# imports
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# home page/index
@app.route("/")
@app.route("/index")
def index():
    recipes = list(mongo.db.recipes.find())
    return render_template("index.html", recipes=recipes)


# sign up function
@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # checks to see if username already exists in mongo database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username Already Taken")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(sign_up)

        # places the user into a session cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign Up Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("sign_up.html")


# login function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checks to see if username exists in mongo database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # checks to see if the username and password match
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # message to tell user, username and password don't match
                flash("Username and/or password incorrect")
                return redirect(url_for('login'))

        else:
            # username is not in the mongo database
            flash("Username and/or password incorrect")
    return render_template("login.html")


# profile function
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


# logout function
@app.route("/logout")
def logout():
    flash("You have logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe")
def add_recipe():
    return render_template("add_recipe.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
