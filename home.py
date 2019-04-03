from flask import Flask, render_template                        #The render template function has been added
from Spotipy_quickstart import get_artist
from food2fork import get_recipe
app = Flask(__name__)                                           #name of module

recipes = [                                                     #made up list for testing
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
    return render_template('home.html', recipes=recipes)        #This returns the render template function for the Home page. See home.html file

#def get_recipes():
 #   recipes=get_recipes()
  #  return render_template('home.html', recipes=recipes)


@app.route('/about/')                                           #This is the flask route to the About page
def about():
    return render_template('about.html', title='About')         #This returns the render template function for the About page. See about.html file

@app.route('/signup/')
def sign_up():
    return render_template('signup.html', title='Sign up')


@app.route('/recipe/<name>/')                                  #This is the flask route to the Artist page
def recipe(name):
    recipes = get_recipe(name)
    recipes = recipes["recipes"]
    return render_template('home.html', recipe_name=name, recipes=recipes)


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

