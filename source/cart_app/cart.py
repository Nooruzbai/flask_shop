from flask import Blueprint, session, flash, redirect, url_for, render_template, request
from flask_login import current_user

from source.cart_app.cart_forms import ItemCartForm
from source.item_app.item_models import Item

cart = Blueprint('cart', __name__)


@cart.route('/cart_list')
def cart_list():
    if 'cart' not in session or not session['cart']:
        flash('Your cart is empty', category='warning')
        # return render_template('cart/cart.html', user=current_user)
        return redirect(url_for('cart.cart_list'))
    return render_template('cart/cart.html', user=current_user)


@cart.route("/add_cart/<int:pk>", methods=['POST'])
def add_cart(pk):
    item = Item.query.get_or_404(pk)
    items_dictionary = {
        str(pk): {'name': item.name, 'price': str(item.price)}
    }
    if 'cart' in session:
        if str(pk) in session['cart']:
            flash(f"{item.name} is already in cart", category='warning')
        session['cart'].update(items_dictionary)
        session.modified = True
    else:
        session['cart'] = items_dictionary
    return redirect(url_for('cart.cart_list'))


@cart.route("/delete_item_from_cart/<int:pk>", methods=['POST'])
def delete_item_from_cart(pk):
    for item_id, item in list(session['cart'].items()):
        if int(item_id) == pk:
            session['cart'].pop(item_id)
            session.modified = True
    return redirect(url_for('cart.cart_list'))


