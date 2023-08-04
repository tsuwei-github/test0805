from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask 2"

@app.route("/test")
def test():
    return "This is test!"


if __name__ == "__main__":
    app.run()
    