from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CreateShopForm(FlaskForm):
    shop_name = StringField("Shop Name", validators=[DataRequired()])
    wifi = StringField("Wifi Rating")
    coffee = StringField("Coffee Rating")
    snacks = StringField("Snacks Rating")
    electrical_outlets = StringField("Electrical outlets availability")
    submit = SubmitField("Submit Coffee Shop")
