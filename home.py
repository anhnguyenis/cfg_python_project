from flask import Flask, render_template                        #The render template function has been added
from Spotipy_quickstart import get_artist
app = Flask(__name__)                                           #name of module

recipes = [
    {
        'author': 'JK Rowling',
        'title': 'Chicken in soup',
    },
    {
        'author': 'Stephen Fry',
        'title': 'Champagne and fromage',
    }
]

@app.route('/')                                                 #This is the flask route to the Home page
@app.route('/home/')                                            #Both these routes return back to the Home page by the same function
def home():
    #return '<h1>This is the Home page!</h1>'
    return render_template('home.html', recipes=recipes)        #This returns the render template function for the Home page. See home.html file

@app.route('/about/')                                           #This is the flask route to the About page
def about():
    #return '<h1>This is the About page</h1>'
    return render_template('about.html')                        #This returns the render template function for the About page. See about.html file


if __name__=='__main__':
    app.run(debug=True)

#@app.route('/artist/<name>/')                                  #This is the flask route to the Artist page
#def home(name):
    #artist=get_artist(name)
    #return render_template('home.html', artist_name=name)

#@app.route('/signup/', methods=["POST"])
#def sign_up():
    #form_data = request.form
    #print (form_data["email"])
    #return "All OK"

