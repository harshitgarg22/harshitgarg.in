import json
import sys
from bs4 import BeautifulSoup as BSHTML, Comment
import re
import subprocess
import os

def stripFilms(filmRawData):
    """
        Returns a files list containing stripped-down output from a letterboxd json file
    
        Keyword Arguments:
        filmRawData: Raw JSON letterboxd data.
    """

    films = []
    open('./error.json', 'w').close()
    for eachFilm in filmRawData["entries"]:
        try:
            rawHTML = BSHTML(eachFilm.get("summary"), 'html.parser')
            
            review = []
            for eachPara in rawHTML.find_all('p')[1:]:
                for eachEle in eachPara.contents:
                    review.append(str(eachEle))
                review.append('<p/>')

            imgsrc = BSHTML(eachFilm.get("summary"), 'html.parser').find('img')['src']
            
            films.append({
            "title": eachFilm.get("letterboxd_filmtitle"),
            "year": eachFilm.get("letterboxd_filmyear"), 
            "link": eachFilm.get("link"),
            "watcheddate": eachFilm.get("letterboxd_watcheddate"),
            "rewatch": eachFilm.get("letterboxd_rewatch"),
            "rating": eachFilm.get("letterboxd_memberrating"),
            "summary": review,
            "imgsrc": imgsrc,
            })
        except:
            with open('./error.json', 'a') as f:
                e = sys.exc_info()
                f.write(str(e) + json.dumps(eachFilm) + '\n')

    return films