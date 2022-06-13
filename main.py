import os
from forms import CreateShopForm
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
    overall = db.Column(db.String(10), nullable=True)

db.create_all()


@app.route('/')
def home():
    shops = Cafe.query.all()
    return render_template('index.html', shops=shops)


@app.route('/add_shop', methods=['GET', 'POST'])
def add_shop():
    form = CreateShopForm()
    if form.validate_on_submit():
        w = float(len(form.wifi.data))
        x = float(len(form.coffee.data))
        y = float(len(form.snacks.data))
        z = float(len(form.electrical_outlets.data))

        overall_rating = round((w + x + y + z)/4)
        overall = overall_rating * "⭐"

        new_shop = Cafe(
            shop_name=form.shop_name.data,
            wifi=form.wifi.data,
            coffee=form.coffee.data,
            snacks=form.snacks.data,
            electrical_outlets=form.electrical_outlets.data,
            overall=overall
        )
        db.session.add(new_shop)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("create_shop.html", form=form)


@app.route('/shop_view/<int:shop_id>')
def view_shop():
    pass


@app.route('/edit_shop/<int:shop_id>', methods=['GET', 'POST'])
def edit_shop(shop_id):
    shop = Cafe.query.get(shop_id)
    edit_form = CreateShopForm(
        shop_name=shop.shop_name,
        wifi=shop.wifi,
        coffee=shop.coffee,
        snacks=shop.snacks,
        electrical_outlets=shop.electrical_outlets,
    )
    if edit_form.validate_on_submit():
        shop.shop_name = edit_form.shop_name.data
        shop.wifi = edit_form.wifi.data
        shop.coffee = edit_form.coffee.data
        shop.snacks = edit_form.snacks.data
        shop.electrical_outlets = edit_form.electrical_outlets.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("create_shop.html", form=edit_form)
#validate on submit works for patches to


@app.route('/delete_shop/<int:shop_id>')
def delete_shop(shop_id):
    shop_to_delete = Cafe.query.get(shop_id)
    db.session.delete(shop_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
