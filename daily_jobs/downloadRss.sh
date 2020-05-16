curl 'https://letterboxd.com/harshitgarg/rss/' -o ~/harshitgarg.in/cgi-bin/assets/data/letterboxd_rss.xml
curl 'https://www.goodreads.com/review/list_rss/55080672?key=XIW0JjwFXykFcPT-nxG_Qf-nhtzXR6JzVXl7eqk9PJ4w_8iQ&shelf=currently-reading' -o ~/harshitgarg.in/cgi-bin/assets/data/goodreads_rss.xml

source ~/harshitgarg.in/cgi-bin/.venv/bin/activate
python3 ~/harshitgarg.in/daily_jobs/jsonDumpFilm.py
