from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class CreateShopForm(FlaskForm):
    shop_name = StringField("Shop Name", validators=[DataRequired()])
    wifi = SelectField("wifi Rating", choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    coffee = SelectField("Coffee Rating", choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    snacks = SelectField("Snacks Rating", choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    electrical_outlets = SelectField("Electrical outlets availability", choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    submit = SubmitField("Submit Coffee Shop")
