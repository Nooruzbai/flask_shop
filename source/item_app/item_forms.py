from datetime import datetime

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import (StringField, SubmitField, DecimalField)
from wtforms.validators import Length, EqualTo, DataRequired, Email, NumberRange


class ItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
    price = DecimalField('Price', places=2, validators=[NumberRange(min=0, max=1000000)])
    image = FileField('Avatar', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
    submit = SubmitField('Submit')



