from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email

class AvengerInfo(FlaskForm):
    hero_name = StringField('Hero name', validators=[DataRequired()])
    legal_name = StringField('Legal Name', validators=[DataRequired()])
    skills = TextAreaField('Skills description', validators=[DataRequired()])
    num = StringField('Phone Number', validators=[DataRequired()])
    submit = SubmitField()

class UserInfo(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()
