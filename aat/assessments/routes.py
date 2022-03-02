from . import assessments


@assessments.route("/")
def index():
    return "All assessments"
