import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from " + os.environ.get("GREETING", "default")

@app.route("/crash")
def crash():
    raise Exception("Deliberate failure")
