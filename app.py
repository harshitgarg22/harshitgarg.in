from flask import Flask, render_template, url_for, redirect, send_file
import json
import os
import datetime
import sentry_sdk 
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(dsn="https://4ca333b6023a4503a94b63b58f1b775c@o391718.ingest.sentry.io/5238246", integrations=[FlaskIntegration()])

app = Flask(__name__, static_folder="./assets", static_url_path="/static")

if __name__ == "main":
    app.run(host="0.0.0.0")

@app.route("/")
def home():
    greetings = generateGreetings()
    projects = getProjects()
    films = getFilms()
    internships = getInternships()
    
    return render_template("index.html", greetings=greetings, projects=projects, films=films, internships=internships)

@app.route("/saumi")
def saumi():
    return render_template("saumi.html")

@app.route("/afort")
def afort():
    return (
        "<html><body>AFORT is currently not available to the general public. If you have any queries, mail at: <em>f20180218@pilani.bits-pilani.ac.in</em></body></html>"
    )

@app.route("/quantum")
def quantum():
    return redirect("https://github.com/harshitgarg22/quantum")

@app.route("/resume")
@app.route("/cv")
def resume():
    return send_file(os.path.join('.','assets', 'docs', 'cv.pdf'))

@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    try:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        return date.strftime("%b %d, %Y")
    except TypeError:
        print(TypeError)

def getFilms():
    films = []

    with open(os.path.join("assets", "data", "filmData.json"), "r") as f:
        films = json.load(f)

    return films

def getProjects():
    projects = []

    projects.append({
        "name": "AFORT",
        "description": "A web repository of Attack Trees. This is part of the work I'm doing under Prof. Rajesh Kumar of BITS Pilani for attack trees.",
        "github": "https://github.com/harshitgarg22/afort",
        "link": url_for('afort'),
        "tags": ["html", "css", "javascript", "attack-trees", "flask"]
    })

    projects.append({
        "name": "learn-quantum",
        "description": "My misadventures as I try to measure a qubit.",
        "github": "https://github.com/harshitgarg22/quantum",
        "link": url_for('quantum'),
        "tags": ["python", "qiskit", "quantum-computing"]
    })

    return projects


def getInternships():
    internships = []

    internships.append({
        "name": "Practice School-1",
        "company": "UST Global, Trivandrum",
        "project_name": "Quantum Distribution Networks",
        "project_begin": "2020-05-18",
        "project_end": "Present",
        "description": "We are currently studying about the possibilites of migrating the current Public Key Infrastructure to become \"Quantum Safe\"."
    })

    return internships


def generateGreetings():
    greetings = {}

    DISPLAY_TEXT = '"Hello World!"'
    greetings["languages"] = ["JavaScript", "C++", "C", "python", "bash"]
    # greetings["headers"] = ["", "#include <iostream>", "#include <stdio.h>", "", ""]
    greetings["display_text"] = DISPLAY_TEXT
    greetings["commands_prefix"] = [
        "console.log(",
        "cout<<",
        "printf(",
        "print(",
        "echo ",
    ]
    greetings["commands_suffix"] = [");", ";", ");", ")", ""]

    return greetings