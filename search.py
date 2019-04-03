from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search = StringField('Type in all your ingredients here (separate each ingredient with a comma ,)', validators=[DataRequired()])
    #password = PasswordField('Password', validators=[DataRequired()])
    #remember_me = BooleanField('Remember Me')
    submit = SubmitField('Search')