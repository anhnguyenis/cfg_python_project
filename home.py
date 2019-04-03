from flask import Flask, render_template                        #The render template function has been added
from food2fork import get_recipe
app = Flask(__name__)                                           #name of module

from search import LoginForm
from flask import render_template, flash, redirect

app.config['SECRET_KEY'] = 'hfdjskahfdjklsaghfdjkaht'

#def get_recipes():
 #   recipes=get_recipes()
  #  return render_template('home.html', recipes=recipes)


@app.route('/about/')                                           #This is the flask route to the About page
def about():
    return render_template('about.html', title='About')         #This returns the render template function for the About page. See about.html file

@app.route('/signup/')
def sign_up():
    return render_template('signup.html', title='Sign up')

@app.route('/home/<name>/')                                     #This is the flask route to the recipe page
def recipe(name):
    recipes = get_recipe(name)
    recipes = recipes["recipes"]
    return render_template('home.html', recipe_name=name, recipes=recipes)

@app.route('/search', methods=['GET', 'POST'])                  #This is the flask route to the search page
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/home/{}'.format(form.search.data))
    return render_template('search.html', title='search ingredient', form=form)

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

