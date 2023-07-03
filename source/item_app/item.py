from flask import render_template, Blueprint, redirect, request, session, url_for, flash
from flask_login import login_required, current_user
from source.extensions import db
from source.item_app.item_forms import ItemForm
from source.item_app.item_models import Item

item = Blueprint('item', __name__)


@item.route("/")
@item.route('/home')
@login_required
def home_page():
    items = Item.query.all()
    return render_template('index.html', items=items, user=current_user)


@item.route('/add_item', methods=['GET', 'POST'])
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        new_item = Item(name=name, price=price)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('item.home_page'))
    return render_template('items/create.html', form=form, user=current_user)


@item.route('/item_details/<int:pk>')
def item_details(pk):
    item = Item.query.get_or_404(pk)
    return render_template('items/detail.html', item=item, user=current_user)

@item.route('/item_delete/<int:pk>')
def item_delete(pk):
    item = Item.query.get_or_404(pk)
    db.session.delete(item)
    db.session.commit()
    flash('The item was deleted!')
    return render_template('items/detail.html', item=item, user=current_user)




