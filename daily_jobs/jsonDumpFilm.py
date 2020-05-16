from stripFilms import stripFilms
import feedparser as fp
import json
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_LOCATION = os.path.join(THIS_FOLDER, "..", "cgi-bin", "assets", "data")

jsonOutput = fp.parse(os.path.join(DATA_LOCATION, "letterboxd_rss.xml"), "r")
films = stripFilms(jsonOutput)

with open(os.path.join(DATA_LOCATION, "filmData.json"), "w") as filmData:
    filmData.write(json.dumps(films))
