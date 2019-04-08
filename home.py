from flask import Flask, render_template, url_for, flash, redirect  #imports render template function from flask and url for
from food2fork import get_recipe                                    #imports the get_recipe function from python file food2fork.py
app = Flask(__name__)                                               #name of module
from search import SearchForm                                       #imports the SearchForm function from python file search.py

app.config['SECRET_KEY'] = 'hfdjskahfdjklsaghfdjkaht'


@app.route('/')                                                 #flask route to the home.html page
def home():
    return render_template('home.html')

@app.route('/recipe/<name>/')                                   #flask route to the recipe_details.html page
def recipe(name):
    recipes = get_recipe(name)
    recipes = recipes["recipes"]
    return render_template('recipe.html', recipe_name=name, recipes=recipes)

@app.route('/search', methods=['GET', 'POST'])                  #flask route to the search.html page
@app.route('/')
def search():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect('/recipe/{}'.format(form.search.data))
    return render_template('search.html', title='search ingredient', form=form)

@app.route('/about/')                                           #flask route to the About page
def about():
    return render_template('about.html', title='About')         #returns the render template function for the about.html file

@app.route('/signup/')
def sign_up():
    return render_template('signup.html', title='Sign up')

if __name__=='__main__':
    app.run(debug=True)





#@app.route('/artist/<name>/')                                  #flask route to the Artist page
#def home(name):
    #artist=get_artist(name)
    #return render_template('home.html', artist_name=name)

#def get_recipes():
 #   recipes=get_recipes()
  #  return render_template('home.html', recipes=recipes)

#@app.route('/signup/', methods=["POST"])
#def sign_up():
    #form_data = request.form
    #print (form_data["email"])
    #return "All OK"

