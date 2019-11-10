from flask import make_response
from flask import current_app as app

@app.route("/")
def index():
    return make_response({"success": True},200)
