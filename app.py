from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/july")
def july_cony():
    return "<p>July con y!!</p>"