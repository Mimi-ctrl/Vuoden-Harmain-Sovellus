from app import app

from flask import redirect, render_template

@app.route("/")
def index():
    return "testi"