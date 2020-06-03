from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class AvengerInfo(FlaskForm):
    hero_name = StringField('Hero name', validators=[DataRequired()])
    legal_name = StringField('Legal Name', validators=[DataRequired()])
    skills = TextAreaField('Skills description', validators=[DataRequired()])
    num = StringField('Phone Number', validators=[DataRequired()])
    submit = SubmitField()