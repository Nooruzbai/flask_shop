import os

from flask import render_template, Blueprint, redirect, url_for, flash, current_app, jsonify
from flask_login import login_required, current_user
from flask_wtf.csrf import generate_csrf
from werkzeug.utils import secure_filename

from source.auth_app.utils import admin_permission
from source.extensions import db
from source.item_app.item_forms import ItemForm
from source.item_app.item_models import Item, item_user

item = Blueprint('item', __name__)


@item.route("/")
@item.route('/home')
@login_required
def home_page():
    items = Item.query.all()
    return render_template('index.html', items=items, user=current_user)


@item.route('/add_item', methods=['GET', 'POST'])
@admin_permission
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        new_item = Item(name=name, price=price)
        uploaded_file = form.image.data
        filename = secure_filename(uploaded_file.filename)
        image_path = os.path.join(current_app.config['UPLOAD_PATH'], filename)
        new_item.image = image_path
        path_list = new_item.image.split('/')[1:]
        new_path = "/".join(path_list)
        new_item.image = new_path
        uploaded_file.save(image_path)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('item.home_page'))
    return render_template('items/create.html', form=form, user=current_user)


@item.route('/item_details/<int:pk>')
def item_details(pk):
    item = Item.query.get_or_404(pk)
    extra_content = {"image_path": None}
    if item.image:
        image_path = item.image.strip('static/')
        extra_content['image_path'] = image_path
    elif not item.image:
        extra_content['image_path'] = 'uploads/blank.png'
    return render_template('items/detail.html', item=item, image_path=extra_content, user=current_user)


@item.route('/item_delete/<int:pk>',  methods=['POST'])
@admin_permission
def item_delete(pk):
    queried_item = Item.query.get_or_404(pk)
    db.session.delete(queried_item)
    db.session.commit()
    flash('The item was deleted!')
    return redirect(url_for('item.home_page', item=item, user=current_user))



@item.route('/update_item/<int:pk>', methods=['GET', 'POST'])
@admin_permission
def update_item(pk):
    form = ItemForm()
    item = Item.query.get_or_404(pk)
    if form.validate_on_submit():
        item.name = form.name.data
        item.price = form.price.data
        uploaded_file = form.image.data
        filename = secure_filename(uploaded_file.filename)
        image_path = os.path.join(current_app.config['UPLOAD_PATH'], filename)
        item.image = image_path
        path_list = item.image.split('/')[1:]
        new_path = "/".join(path_list)
        item.image = new_path
        uploaded_file.save(image_path)
        db.session.add(item)
        db.session.commit()
        flash(f"You have upadated item {item.name}", category='success')
        return redirect(url_for('item.home_page'))
    form.name.data = item.name
    form.price.data = item.price
    return render_template('items/update.html', form=form, user=current_user)


@item.route('/favorite/<int:pk>', methods=["GET", "POST"])
def favorite(pk):
    query_item = Item.query.get_or_404(pk)
    print(query_item)
    if query_item.favorited_users.filter_by(id=current_user.id).first():
        query_item.favorited_users.remove(current_user)
        db.session.commit()
        button_text = 'Favorite'
    else:
        query_item.favorited_users.append(current_user)
        db.session.commit()
        button_text = 'Unfavorite'
    return {'value': button_text}






