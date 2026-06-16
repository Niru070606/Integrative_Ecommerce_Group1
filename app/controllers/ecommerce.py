from flask import Blueprint,render_template, request, redirect, url_for, flash
from app.models.ecommerce import Ecommerce
from app import db

product_bp = Blueprint('product',__name__)

@product_bp.route("/")
def main():
    return render_template('public/main.html')

@product_bp.route('/product')
def product():
    return render_template('public/product.html')

@product_bp.route('/deals')
def deals():
    return render_template('public/deals.html')

@product_bp.route('/contact')
def contact():
    return render_template('public/contact.html')


@product_bp.route('/secondPage')
def secondPage():
    products = Ecommerce.query.all() # Ask Model for all records
    return render_template('public/secondPage.html', products=products)

@product_bp.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Ecommerce.query.get(product_id)# Ask Model for one record
    return render_template('public/product_templates/details.html', product=product)

@product_bp.route('/adminList')
def adminList():
    products = Ecommerce.query.all()
    return render_template('public/adminList.html', products=products)

@product_bp.route('/<int:product_id>/edit', methods = ['GET', 'POST'])
def edit_product(product_id):
    product = Ecommerce.query.get(product_id)

    if product is None:
        flash('Product not found', 'error')
        return redirect(url_for('product.adminList'))

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_description = request.form.get('product_details')
        file_path = request.form.get('file_path')
        price = request.form.get('price')
        category = request.form.get('category')
        stocks = request.form.get('stocks')
        specification = request.form.get('specification')

        if not product_name or not product_description or not file_path or not price or not category or not stocks or not specification:
            flash('All fields required to be filled', 'error')
            return redirect(url_for('product.edit_product', product_id=product.id))
        
        product.product_name = product_name
        product.product_description = product_description
        product.file_path = file_path
        product.price = price
        product.category = category
        product.stocks = stocks
        product.specification = specification

        db.session.commit()

        flash('Succesfully edited the product', 'succes')
        return redirect(url_for('product.edit_product', product_id=product.id))
    return render_template('public/edit_product.html', product=product)




@product_bp.route('/addProduct', methods = ['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_description = request.form.get('product_details')
        file_path = request.form.get('file_path')
        price = request.form.get('price')
        category = request.form.get('category')
        stocks = request.form.get('stocks')
        specification = request.form.get('specification')

        if not product_name or not product_description or not file_path or not price or not category or not stocks or not specification:
            flash('All fields required to be filled', 'error')
            return redirect(url_for('product.add_product'))
        
        new_product = Ecommerce(product_name=product_name, product_description=product_description, file_path=file_path, price=price, category=category, stocks=stocks, specification=specification)
        db.session.add(new_product)
        db.session.commit()

        flash('Succesfully added a new product', 'succes')
        return redirect(url_for('product.adminList'))
    
    return render_template('public/add_products.html')

@product_bp.route('/<int:product_id>/delete', methods = ['GET', 'POST'])
def delete_product(product_id):
    product = Ecommerce.query.get(product_id)

    if product is None:
        flash('Product not found', 'error')
        return redirect(url_for('product.adminList'))

    if request.method == 'POST':
        db.session.delete(product)
        db.session.commit()
        
        flash(f'{product.product_name} has been deleted', 'succes')
        return redirect(url_for('product.adminList'))
    
    return render_template('public/confirm_delete.html', product=product)
    