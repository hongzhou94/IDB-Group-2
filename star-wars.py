from flask import Flask, render_template
from models import Film, Character, Planet
import json
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Splash page"


@app.route('/films')
def films():
    f_name = os.path.join(app.static_folder, 'Films.json')
    with open(f_name) as f:
        data = json.load(f)

    f1 = Film(data['results'][0]['title'], data['results'][0]['director'], data['results'][0]['producer'], data['results'][0]['episode_id'], "http://cdn2us.denofgeek.com/sites/denofgeekus/files/starwars-iv.jpg")
    f2 = Film(data['results'][1]['title'], data['results'][1]['director'], data['results'][1]['producer'], data['results'][1]['episode_id'], "https://i.ytimg.com/vi/jDIHiIxUGEY/maxresdefault.jpg")
    f3 = Film(data['results'][2]['title'], data['results'][2]['director'], data['results'][2]['producer'], data['results'][2]['episode_id'], "http://static.dolimg.com/lucas/movies/starwars/starwars_epi5_01-de788d5a9549.jpg")
    films_list = [f1, f2, f3]

    return render_template('films.html', films=films_list)

# TODO: Grab images from Bing Image search api

@app.route('/characters')
def characters():
    return render_template('characters.html')


@app.route('/planets')
def planets():
    return render_template('planets.html')


if __name__ == '__main__':
    app.run(debug=True)
