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
            # A really complex parsing with no documentation and bad variable name muhahahahahahaha
            soup = (''.join(str(y) for a in [x.contents for x in BSHTML(eachFilm.get("summary"), 'html.parser').find_all('p')[1:]] for y in a)).replace('<br/>', '\n\n')
            imgsrc = BSHTML(eachFilm.get("summary"), 'html.parser').find('img')['src']
            
            films.append({
            "title": eachFilm.get("letterboxd_filmtitle"),
            "year": eachFilm.get("letterboxd_filmyear"), 
            "link": eachFilm.get("link"),
            "watcheddate": eachFilm.get("letterboxd_watcheddate"),
            "rewatch": eachFilm.get("letterboxd_rewatch"),
            "rating": eachFilm.get("letterboxd_memberrating"),
            "summary": str(soup),
            "imgsrc": imgsrc,
            })
        except:
            with open('./error.json', 'a') as f:
                e = sys.exc_info()
                f.write(str(e) + json.dumps(eachFilm) + '\n')

    return films