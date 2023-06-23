from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Flask'


@app.route('/search4/')
def search4letters(phrase ='life,the universe,and everything', letters = 'eiru!') -> set:
    """Return the letters which are common with phrase"""
    return str(set(letters).intersection(set(phrase)))


app.run()
