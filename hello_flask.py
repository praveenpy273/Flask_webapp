from flask import Flask
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Flask'

@app.route('/search4')
def do_search():
    return str(search4letters('life, the universe, and everything', 'eiru!'))


app.run()