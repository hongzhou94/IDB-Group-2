from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/films')
def models():
    return render_template('films.html')


@app.route('/characters')
def models():
    return render_template('characters.html')


@app.route('/planets')
def models():
    return render_template('planets.html')


if __name__ == '__main__':
    app.run(debug=True)
