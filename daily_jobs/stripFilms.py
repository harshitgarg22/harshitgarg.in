import json
import sys

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
            "published": eachFilm.get("published"),
            "watcheddate": eachFilm.get("letterboxd_watcheddate"),
            "rewatch": eachFilm.get("letterboxd_rewatch"),
            "rating": eachFilm.get("letterboxd_memberrating"),
            "summaryHTML": eachFilm.get("summary"),
            "author": eachFilm["author"]
            })
        except KeyError:
            with open('./error.json', 'a') as f:
                f.write(str(KeyError) + json.dumps(eachFilm) + '\n')

    return films