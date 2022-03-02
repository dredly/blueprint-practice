from flask import Flask
from .assessments import assessments
from .users import users

app = Flask(__name__)

app.register_blueprint(assessments, url_prefix="/assessments")
app.register_blueprint(users)
