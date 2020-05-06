import json
import sys
from bs4 import BeautifulSoup as BSHTML, Comment
import re
import subprocess
import os

def sanitize_html(html):
    """
        Returns sanitize html to protect against XSS
    """
    # God bless https://chase-seibert.github.io/blog/2011/01/28/sanitize-html-with-beautiful-soup.html

    if not html:
        return None

    blacklist = ["script", "style", "img"]

    soup = BSHTML(html, 'html.parser')        
    # now strip HTML we don't like.
    for tag in soup.findAll():
        if tag.name.lower() in blacklist:
            # blacklisted tags are removed in their entirety
            tag.extract()
        else:
            tag.attrs = []

    # scripts can be executed from comments in some cases
    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    for comment in comments:
        comment.extract()

    safe_html = soup

    if safe_html == ", -":
        return None

    return safe_html


def _attr_name_whitelisted(attr_name):
    return attr_name.lower() in ["href", "style", "color", "size", "bgcolor", "border", ""]

def safe_css(attr, css):
    if attr == "style":
        return re.sub("(width|height):[^;]+;", "", css)
    return css

def stripFilms(filmRawData):
    """
        Returns a files list containing stripped-down output from a letterboxd json file
    
        Keyword Arguments:
        filmRawData: Raw JSON letterboxd data.
    """

    films = []
    open('./error.json', 'w').close()
    for eachFilm in filmRawData["entries"]:
        safe_html = BSHTML(eachFilm.get("summary"), 'html.parser')
        try:
            # A really complex parsing with no documentation and bad variable name muhahahahahahaha
            # soup = (''.join(str(z) for a in [x for x in safe_html.find_all('p')] for z in a))
            soup = [y for x in safe_html.find_all('p')[1:] for y in x.contents]
            # soup = []
            # review = (''.join(str(y) for a in [x.contents for x in safe_html.find_all('p')[1:]] for y in a)).replace('<br/>', '\n\n')
            review = str(soup)
            # for x in safe_html.find_all('p')[1:]:
            #     for y in x.contents:
            #         soup.append(y)

            # review = ''
            # for x in soup:
            #     review = review + (str(x))


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