class Film:
    def __init__(self, title, director, producer, episode_no, release_date, characters, planets, img_url):
        self.title = title
        self.director = director
        self.producer = producer
        self.episode_no = episode_no
        self.release_date = release_date
        self.characters = characters
        self.planets = planets
        self.img_url = img_url
        self.characters = characters
        self.planets = planets


class Character:
    def __init__(self, name, birth_year, height, mass, films, planets, img_url):
        self.name = name
        self.birth_year = birth_year
        self.height = height
        self.mass = mass
        self.films = films
        self.planets = planets
        self.img_url = img_url
        self.films = films
        self.planets = planets


class Planet:
    def __init__(self, name, climate, population, gravity, terrain, films, characters, img_url):
        self.name = name
        self.climate = climate
        self.population = population
        self.gravity = gravity
        self.terrain = terrain
        self.films = films
        self.characters = characters
        self.img_url = img_url
        self.films = films
        self.characters = characters

