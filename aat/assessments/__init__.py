from flask import Blueprint

assessments = Blueprint(
    "assessments", __name__, template_folder="templates", static_folder="static"
)

from . import routes
