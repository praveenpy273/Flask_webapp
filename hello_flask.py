from flask import Flask, render_template, request
from vsearch import search4letters

'''__name__ when used anywhere in the code it dentoes currently active module
Flask class needs to know the name of currently active module'''
app = Flask(__name__)



@app.route('/search4',methods=['POST'])
def do_search() -> str: 
    phrase = request.form['phrase']
    letters = request.form['letters']
    """Return the letters which are common with phrase"""
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_title = title,
                           the_phrase = phrase,
                           the_letters= letters,
                           the_results = results,)

@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title = 'Welcome to search4letters on the web!')


if __name__ == '__main__':
    app.run(debug = True)
