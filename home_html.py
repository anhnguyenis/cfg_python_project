from flask import Flask, render_template
from Spotipy_quickstart import get_artist


app = Flask(__name__)


@app.route('/artist/<name>/')
def home(name):
    artist=get_artist(name)

    return render_template('home.html', artist_name=name)
app.run(debug=True)