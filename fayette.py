import json
import requests
import datetime

from flask import Flask, render_template

app = Flask(__name__)

MEETUP_GROUP_URLNAME = 'FayettePy-Python-Meetup'
MEETUP_API_KEY = '555a61807e631511307615d604e7448'

@app.route("/")
def index():
    """
    This is the index view for FayettePy.
    It is loaded at "/"
    """

    return render_template("index.html")


@app.route("/members")
def members():
    # Get members from Meetup's API
    member_endpoint = "https://api.meetup.com/2/members/"
    params = {
        'sign': True,
        'key': MEETUP_API_KEY,
        'group_urlname': MEETUP_GROUP_URLNAME
    }

    response = requests.get(member_endpoint, params)
    api_members = json.loads(response.content)

    members = []
    for m in api_members['results']:
        members.append({
            'name': m.get('name', None),
            'photo': m.get('photo', None),
            'bio': m.get('bio', None),
        })

    return render_template('members.html', members=members)



@app.route("/events")
def events():
    """
    This is the index view for FayettePy.
    It is loaded at "/"
    """
    # Get events from Meetup's API
    events_endpoint = "https://api.meetup.com/2/events/"
    params = {
        'sign': True,
        'key': MEETUP_API_KEY,
        'group_urlname': MEETUP_GROUP_URLNAME
    }

    response = requests.get(events_endpoint, params)
    api_events = json.loads(response.content)

    events = []
    for e in api_events['results']:
        date = datetime.datetime.fromtimestamp(e.get('time', None) / 1000)

        events.append({
            'name': e.get('name', None),
            'url': e.get('event_url', None),
            'venue': e.get('venue', None),
            'date': date.strftime("%A, %B %d, %Y at %I:%S %p"),
            'description': e.get('description', None),
        })

    return render_template("events.html", events=events)

if __name__ == '__main__':
    app.debug = True
    app.run()
