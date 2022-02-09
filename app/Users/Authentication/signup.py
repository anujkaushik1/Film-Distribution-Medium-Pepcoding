from app import app
from flask import request

@app.route("/signup", methods = ["POST"])
def signUp():
    user = request.json
    
    return user