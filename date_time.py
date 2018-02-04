from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'
@app.route('/search4')
def do_search():
    return str('balakrishna')

@app.route('/entry')
def entry_page():
    return render_template('entry.html',the_title='Welcome to search4letters on the web!')


app.run()
