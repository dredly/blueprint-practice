from . import users
from flask import render_template


@users.route("/login")
def login():
    return render_template("login.html")


@users.route("/register")
def register():
    return render_template("register.html")
