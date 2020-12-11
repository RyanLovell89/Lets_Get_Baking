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
    return render_template("index.html")


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
    recipes = list(mongo.db.recipes.find())
    return render_template("profile.html", username=username, recipes=recipes)


# logout function
@app.route("/logout")
def logout():
    flash("You have logged out")
    session.pop("user")
    return redirect(url_for("login"))


# add recipe function
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "baking_time": request.form.get("baking_time"),
            "preparation_time": request.form.get("preparation_time"),
            "ingredient_one": request.form.get("ingredient_one"),
            "ingredient_two": request.form.get("ingredient_two"),
            "ingredient_three": request.form.get("ingredient_three"),
            "ingredient_four": request.form.get("ingredient_four"),
            "ingredient_five": request.form.get("ingredient_five"),
            "ingredient_six": request.form.get("ingredient_six"),
            "ingredient_seven": request.form.get("ingredient_seven"),
            "ingredient_eight": request.form.get("ingredient_eight"),
            "weight_one": request.form.get("weight_one"),
            "weight_two": request.form.get("weight_two"),
            "weight_three": request.form.get("weight_three"),
            "weight_four": request.form.get("weight_four"),
            "weight_five": request.form.get("weight_five"),
            "weight_six": request.form.get("weight_six"),
            "weight_seven": request.form.get("weight_seven"),
            "weight_eight": request.form.get("weight_eight"),
            "weight_nine": request.form.get("weight_nine"),
            "weight_ten": request.form.get("weight_ten"),
            "instruction_one": request.form.get("instruction_one"),
            "instruction_two": request.form.get("instruction_two"),
            "instruction_three": request.form.get("instruction_three"),
            "instruction_four": request.form.get("instruction_four"),
            "instruction_five": request.form.get("instruction_five"),
            "instruction_six": request.form.get("instruction_six"),
            "added_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Your Recipe Has Been Added")
        # sends the user to their profile when recipe added
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        return redirect(url_for("profile", username=username))

    return render_template("add_recipe.html")


# edit function
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        edit = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "baking_time": request.form.get("baking_time"),
            "preparation_time": request.form.get("preparation_time"),
            "ingredient_one": request.form.get("ingredient_one"),
            "ingredient_two": request.form.get("ingredient_two"),
            "ingredient_three": request.form.get("ingredient_three"),
            "ingredient_four": request.form.get("ingredient_four"),
            "ingredient_five": request.form.get("ingredient_five"),
            "ingredient_six": request.form.get("ingredient_six"),
            "ingredient_seven": request.form.get("ingredient_seven"),
            "ingredient_eight": request.form.get("ingredient_eight"),
            "weight_one": request.form.get("weight_one"),
            "weight_two": request.form.get("weight_two"),
            "weight_three": request.form.get("weight_three"),
            "weight_four": request.form.get("weight_four"),
            "weight_five": request.form.get("weight_five"),
            "weight_six": request.form.get("weight_six"),
            "weight_seven": request.form.get("weight_seven"),
            "weight_eight": request.form.get("weight_eight"),
            "instruction_one": request.form.get("instruction_one"),
            "instruction_two": request.form.get("instruction_two"),
            "instruction_three": request.form.get("instruction_three"),
            "instruction_four": request.form.get("instruction_four"),
            "instruction_five": request.form.get("instruction_five"),
            "instruction_six": request.form.get("instruction_six"),
            "added_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edit)
        flash("Your Recipe Has Been Edited")
        # takes the user back to the profile
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        return redirect(url_for("profile", username=username))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


# delete function
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Your Recipe Has Been Deleted")
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    return redirect(url_for("profile", username=username))


# recipe book
@app.route("/recipe_book", methods=["GET", "POST"])
def recipe_book():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipe_book.html", recipes=recipes)


# search function
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipe_book.html", recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
