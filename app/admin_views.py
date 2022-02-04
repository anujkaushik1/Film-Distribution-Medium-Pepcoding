from app import app

@app.route("/admin")
def indexing():
    return "<h1> Hello Admin </h1>"