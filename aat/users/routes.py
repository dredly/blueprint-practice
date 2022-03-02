from . import users


@users.route("/login")
def login():
    return "Supposedly logging in"


@users.route("/register")
def register():
    return "Supposedly registering"
