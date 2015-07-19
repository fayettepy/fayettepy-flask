from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """
    This is the index view for FayettePy.
    It is loaded at "/"
    """
    return render_template("index.html", color_list=['red', 'green', 'blue'])

@app.route("/members")
def members():
    """
    Load members via the Meetup API
    """
    members = []
    return render_template("members.html", members=members)

@app.route("/events")
def events():
    """
    Load events via the Meetup API
    """
    events = []
    return render_template("events.html", events=events)

if __name__ == '__main__':
    app.debug = True
    app.run()
