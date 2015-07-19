from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """
    This is the index view for FayettePy.
    It is loaded at "/"
    """
    return "<h1>It worked!</h1>"


@app.route("/other-page")
def other_page():
    """
    This is the index view for FayettePy.
    It is loaded at "/"
    """
    return "<h1>This is another page!</h1>"

if __name__ == '__main__':
    app.debug = True
    app.run()
