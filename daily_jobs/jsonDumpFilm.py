from stripFilms import stripFilms
import feedparser as fp
import json
import os

DATA_LOCATION = os.path.join("..", "cgi-bin", "assets", "data")

jsonOutput = fp.parse(os.path.join(DATA_LOCATION, "letterboxd_rss.xml"), "r")
films = stripFilms(jsonOutput)

with open(os.path.join(DATA_LOCATION, "filmData.json"), "w") as filmData:
    filmData.write(json.dumps(films))
