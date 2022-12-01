from app import app

from flask import redirect, render_template, request
from os import getenv
import users

app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def index():
    return render_template("frontpage.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if not users.login(username, password):
        return render_template("errors.html", error="Väärä käyttäjätunnus tai salasana")
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("errors.html", error="Salasanat eivät ole samat")
        if len(password1) < 8:
            return render_template("errors.html",
                                   error="Salasanassa pitää olla vähintään 8 merkkiä")
        if len(password1) > 30:
            return render_template("errors.html", error="Salasanassa saa olla enintään 30 merkkiä")
        users.new_user(username, password1)
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")