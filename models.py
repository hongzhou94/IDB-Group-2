class Film:
    def __init__(self, title, director, producer, episode_no, release_date, img_url):
        self.title = title
        self.director = director
        self.producer = producer
        self.episode_no = episode_no
        self.release_date = release_date
        self.img_url = img_url


class Character:
    def __init__(self, name, birth_year, height, mass, img_url):
        self.name = name
        self.birth_year = birth_year
        self.height = height
        self.mass = mass
        self.img_url = img_url


class Planet:
    def __init__(self, name, climate, population, gravity, terrain, img_url):
        self.name = name
        self.climate = climate
        self.population = population
        self.gravity = gravity
        self.terrain = terrain
        self.img_url = img_url

