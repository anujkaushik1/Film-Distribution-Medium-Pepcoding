from app import app, db, migrate, SQLAlchemyError
from app.models.Authentication import UserModel
from flask import request

@app.route("/signup", methods = ["POST", "GET"])
def signUp():
    
    try:
        if(request.method == "POST"):
            print()
            print()
            print()
            print()
            user = request.json
            name = user["name"]
            email = user["email"]
            password = user["password"]
            id = 1

            newUser = UserModel(id=1,name=name, email=email, password=password)
            db.session.add(newUser)
            data = db.session.commit()
            if(data):
                print(data)

    except SQLAlchemyError as e :

        #    error = str(e.__dict__['orig'])
           print(e)
    
    return "Hello world"