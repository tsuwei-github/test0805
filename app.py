from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask 2"

@app.route("/test")
def test():
    return "This is test!"

@app.route("/test1")
def test1():
    return "This is test11111111!"

@app.route("/test2")
def test2():
    return "This is test2222222222!"


if __name__ == "__main__":
    app.run()