from app import db

class Ecommerce(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    product_description = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    stocks = db.Column(db.Integer, nullable=False)
    specification = db.Column(db.String(2000), nullable=False)


    def __repr__(self):
        return f'<Product {self.product_name}>'
