from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "<h1>Hello, please work</h1>"

@app.route("/driele-linda")
def driele_linda():
  return "<h1>Driele é linda!</h1>"