from flask import render_template
from . import assessments


@assessments.route("/")
def index():
    return render_template("index.html")
