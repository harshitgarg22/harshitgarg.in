from flask import Flask, render_template

app = Flask(__name__, static_folder="./assets", static_url_path="/static")


@app.route("/")
def home():
    return render_template("index.html")
