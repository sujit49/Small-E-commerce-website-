from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import stripe
import requests

# Initialize the Flask app
app = Flask(__name__)

# Configure the database URI (Update with your credentials)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flask_app_db1'
app.config['SECRET_KEY'] = 'pk_test_51QUmR6GGXmMuw14gyFBdHkw9lnMzZFlStePlPkhmguznera8hEffTsypUjBtw6hZUxSgUmLHadE5K9FWImwKEWjl00e2a9ZzZk'  # Change this
db = SQLAlchemy(app)

# Stripe API configuration
stripe.api_key = "sk_test_51QUmR6GGXmMuw14gcvDSMct6s7pMrfSensZLIhwRZB0xO5yas6dWoEefXWFD9tO03dBt7zaUrvf61SrAqAAwQwXH00aOCIlCFM"  # Change this

# Initialize LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# User Loader for LoginManager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Models for Product, CartItem, and User (UserMixin for flask-login)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Product {self.name}>"

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    product = db.relationship('Product', backref='cart_items', lazy=True)

    def __repr__(self):
        return f"<CartItem {self.product.name}, Quantity: {self.quantity}>"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User {self.username}>"

# Routes for home, login, register, etc.

@app.route('/')
def home():
    # Fetch products from an API (Fakestore API)
    response = requests.get("https://fakestoreapi.com/products")
    products = response.json()
    return render_template('home.html', products=products)

@app.route('/add-to-cart/<int:product_id>')
def add_to_cart(product_id):
    if 'user_id' not in session:
        flash('You need to log in first!')
        return redirect(url_for('login'))

    product = Product.query.get(product_id)
    cart_item = CartItem.query.filter_by(user_id=session['user_id'], product_id=product_id).first()

    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = CartItem(user_id=session['user_id'], product_id=product_id, quantity=1)
        db.session.add(cart_item)

    db.session.commit()
    flash('Product added to cart!')
    return redirect(url_for('home'))

@app.route('/cart')
def cart():
    if 'user_id' not in session:
        flash('You need to log in first!')
        return redirect(url_for('login'))

    cart_items = CartItem.query.filter_by(user_id=session['user_id']).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/checkout')
def checkout():
    if 'user_id' not in session:
        flash('You need to log in first!')
        return redirect(url_for('login'))

    cart_items = CartItem.query.filter_by(user_id=session['user_id']).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('checkout.html', total=total)

@app.route('/create-checkout-session', methods=['POST'], endpoint='create-checkout-session')
def create_checkout_session():

    try:
        cart_items = CartItem.query.filter_by(user_id=session['user_id']).all()
        line_items = [{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.product.name,
                },
                'unit_amount': int(item.product.price * 100),
            },
            'quantity': item.quantity,
        } for item in cart_items]

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=url_for('success', _external=True),
            cancel_url=url_for('home', _external=True),
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        return str(e)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            flash('Logged in successfully!')
            return redirect(url_for('home'))
        flash('Invalid credentials!')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registered successfully! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully!')
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=8090)
