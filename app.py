from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from OpenShift!</h1>"

@app.route("/health")
def health():
    return "OK"
