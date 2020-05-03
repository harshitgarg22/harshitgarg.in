import json
import sys
from bs4 import BeautifulSoup as BSHTML

def stripFilms(filmRawData):
    """Returns a files list containing stripped-down output from a letterboxd json file
    
        Keyword Arguments:
        filmRawData: Raw JSON letterboxd data.
    """

    films = []
    open('./error.json', 'w').close()
    for eachFilm in filmRawData["entries"]:
        try:
            films.append({
            "title": eachFilm.get("letterboxd_filmtitle"),
            "year": eachFilm.get("letterboxd_filmyear"), 
            "link": eachFilm.get("link"),
            "watcheddate": eachFilm.get("letterboxd_watcheddate"),
            "rewatch": eachFilm.get("letterboxd_rewatch"),
            "rating": eachFilm.get("letterboxd_memberrating"),
            # "published": eachFilm.get("published"),
            # "imgsrc": imgsrc,
            # "description": text,
            # "author": eachFilm["author"]
            })
        except:
            with open('./error.json', 'a') as f:
                f.write(json.dumps(eachFilm) + '\n')

    return films