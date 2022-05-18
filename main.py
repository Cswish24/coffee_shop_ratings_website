import os

from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "wordpasspasspassword"
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", 'sqlite:///cafe.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Cafe(db.Model):
    __tablename__ = "Coffee Shops"
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(30), nullable=False)
    wifi = db.Column(db.String(10), nullable=True)
    coffee = db.Column(db.String(10), nullable=True)
    snacks = db.Column(db.String(10), nullable=True)
    electrical_outlets = db.Column(db.String(10), nullable=True)


db.create_all()


@app.route('/')
def home():
    shops = Cafe.query.all()
    return render_template("index.html")


@app.route('/coffee_shops')
def shop_list():
    shops = Cafe.query.all()
    return render_template('shops.html', shops=shops)


@app.route('/add_shop', methods=['GET', 'POST'])
def add_shop():
    pass


@app.route('/shop_view/<int:shop_id>')
def view_shop():
    pass


@app.route('/edit_shop/<int:shop_id>', methods=['GET', 'PATCH'])
def edit_shop(shop_id):
    pass
#validate on submit works for patches to


@app.route('/delete_shop/<int:shop_id>', methods=['GET', 'DELETE'])
def delete_shop(shop_id):
    pass

if __name__ == "__main__":
    app.run(debug=True)
