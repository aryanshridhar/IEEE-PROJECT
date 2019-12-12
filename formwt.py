from flask_wtf import FlaskForm 
from wtforms import StringField , SubmitField , IntegerField , BooleanField , RadioField
from wtforms.validators import Length,  Email , DataRequired , NumberRange 

class Represent(FlaskForm):
    name = StringField('name' , validators=[DataRequired(),Length(min = 1 , max = 20)])
    username = StringField('username' , validators=[DataRequired() , Length(min = 2 , max = 20)])
    age = IntegerField('age' , validators=[DataRequired() , NumberRange(min=18)])
    button = SubmitField('Register Me !')

class Vote(FlaskForm):
    # radio = RadioField('radio' , validators=[DataRequired()], choices=[(1,'Vote')])
    button = SubmitField('Vote !')