from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return "Hello from DO App platform!"

