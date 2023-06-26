from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Flask'


@app.route('/search4')
def do_search(phrase ='life,the universe,and everything', letters = 'eiru!'):
    """Return the letters which are common with phrase"""
    return str(set(letters).intersection(set(phrase)))


app.run()
