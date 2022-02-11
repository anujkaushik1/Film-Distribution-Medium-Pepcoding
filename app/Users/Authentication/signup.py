from genericpath import exists
from app import app, db, migrate, SQLAlchemyError
from app.models.Authentication import UserModel
from flask import jsonify, request

@app.route("/signup", methods = ["POST", "GET"])
def signUp():
    try:
        if(request.method == "POST"):
            user = request.json
            name = user["name"]
            email = user["email"]
            password = user["password"]
            confirmPassword = user["confirmPassword"]

            newUser = UserModel(name=name, email=email, password=password)
            db.session.add(newUser)
            db.session.commit()
            
            res = {
                "success" : True,
                "data" : [
                    {
                        "name" : newUser.name,
                        "email" : newUser.email,
                        "password" : newUser.password
                    }
                ]
            }

            return jsonify(res), 200

            
    except SQLAlchemyError as e :

        error = str(e.__dict__['orig'])

        res = {
            "success" : False,
            "error" : error
        } 

        return jsonify(res), 400
                