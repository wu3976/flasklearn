import flask as fl

app=fl.Flask(__name__)

@app.route("/success/<name>")
def success (name):
    print("Welcome, %s", name)
