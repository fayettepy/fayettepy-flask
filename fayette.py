from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """
    This is the index view for FayettePy.
    It is loaded at "/"
    """
    return render_template("index.html", color_list=['red', 'green', 'blue'])


@app.route("/events")
def events():
    """
    This is the index view for FayettePy.
    It is loaded at "/"
    """
    return "<h1>This is the events page</h1>"

if __name__ == '__main__':
    app.debug = True
    app.run()
