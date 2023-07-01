from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import (StringField, RadioField, EmailField, validators,
                     PasswordField, DateTimeField, SubmitField, DecimalField)
from wtforms.validators import Length, EqualTo, DataRequired, Email, NumberRange


class ItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
    price = DecimalField('Price', places=2, validators=[NumberRange(min=0, max=1000000)])
    submit = SubmitField('Submit')



