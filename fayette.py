from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """
    This is the index view for FayettePy.
    It is loaded at "/"
    """
    return "<h1>It worked!</h1>"

if __name__ == '__main__':
    app.debug = True
    app.run()
