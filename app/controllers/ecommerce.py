from flask import Blueprint,render_template
from app.models.ecommerce import Ecommerce

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


