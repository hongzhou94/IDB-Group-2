from flask import Flask, render_template
from models import Film, Character, Planet
from db_mock import MockDB

app = Flask(__name__)

# for persistence throughout app lifetime
# required for linking between instances
db = MockDB(app.static_folder)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/film/<film_id>')
def film(film_id):
    return render_template('film_instance.html', film=db.get_film(film_id))


@app.route('/films')
def films():
    return render_template('films.html', films=db.get_films())
# TODO: Grab images from Bing Image search api


@app.route('/character/<character_id>')
def character(character_id):
    return render_template('character_instance.html', character=db.get_character(character_id))


@app.route('/characters')
def characters():
    return render_template('characters.html', characters=db.get_characters())


@app.route('/planet/<planet_id>')
def planet(planet_id):
    return render_template('planet_instance.html', planet=db.get_character(planet_id))


@app.route('/planets')
def planets():
    return render_template('planets.html', planets=db.get_planets())


if __name__ == '__main__':
    app.run(debug=True)
