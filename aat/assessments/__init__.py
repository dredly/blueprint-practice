from flask import Blueprint

assessments = Blueprint("assessments", __name__, template_folder="templates")

from . import routes
