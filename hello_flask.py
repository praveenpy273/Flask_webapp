from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Flask'


@app.route('/search4',methods=['POST'])
def do_search(phrase ='life,the universe,and everything', letters = 'eiru,!') -> set:
    """Return the letters which are common with phrase"""
    return str(set(letters).intersection(set(phrase)))

@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title = 'Welcome to search4letters on the web!')


app.run(debug = True)
