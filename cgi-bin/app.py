from flask import Flask, render_template, url_for, redirect
import json
import os
import datetime

app = Flask(__name__, static_folder="./assets", static_url_path="/static")


@app.route("/")
def home():
    greetings = generateGreetings()
    projects = getProjects()
    films = getFilms()

    return render_template("index.html", greetings=greetings, projects=projects, films=films)


@app.route("/afort")
def afort():
    return render_template(
        "<html><body>AFORT is currently not available to the general public. If you have any queries, mail at: <em>f20180218@pilani.bits-pilani.ac.in</em></html>"
    )

@app.route("/quantum")
def quantum():
    return redirect("https://github.com/harshitgarg22/quantum")

def getFilms():
    films = []

    with open(os.path.join("cgi-bin", "assets", "data", "filmData.json"), "r") as f:
        films = json.load(f)

    return films

@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    try:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        return date.strftime("%b %d, %Y")
    except TypeError:
        print(TypeError)

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
    internships = {}

    internships["name"] = []
    internships["description"] = []


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
