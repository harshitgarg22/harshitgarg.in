from flask import Flask, render_template

app = Flask(__name__, static_folder="./assets", static_url_path="/static")


@app.route("/")
def home():
    greetings = generateGreetings()

    return render_template("index.html", greetings=greetings)


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
