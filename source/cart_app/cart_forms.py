from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, validators, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class ItemCartForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
    price = DecimalField('Price', places=2, validators=[NumberRange(min=0, max=1000000)])
    quantity = IntegerField('Quantity', validators=[NumberRange(min=0, max=1000000)])
    submit = SubmitField('Submit')
