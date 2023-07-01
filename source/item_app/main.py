from flask import render_template, Blueprint, redirect, request, session
from flask_login import login_required, current_user
from source.extensions import db
from source.item_app.item_forms import ItemForm
from source.item_app.item_models import Item

main = Blueprint('main', __name__)


@main.route("/")
@main.route('/home')
@login_required
def home_page():
    items = Item.query.all()
    return render_template('index.html', items=items, user=current_user)


@main.route('/add_item', methods=['GET', 'POST'])
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        new_item = Item(name=name, price=price)
        db.session.add(new_item)
        db.session.commit()
    return render_template('webapp/create.html', form=form, user=current_user)


@main.route('/item_details/<int:pk>')
def item_details(pk):
    item = Item.query.get_or_404(pk)
    return render_template('webapp/detail.html', item=item, user=current_user)



@main.route("/add_cart", methods=['GET', 'POST'])
def add_cart():
    pass


