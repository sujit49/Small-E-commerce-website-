# 🛍️ Flask eCommerce Web App

This project is a Python-based eCommerce web application built using **Flask** that allows users to register, log in, browse products fetched from an API, add products to their cart, and make secure payments using **Stripe**. The app uses **MySQL** for backend storage and includes robust session handling, secure password hashing, and seamless checkout integration.

---

## Features

- **User Management:**
  - User registration with hashed passwords
  - User login and logout
  - Session management using Flask-Login

- **Product Catalog:**
  - Products fetched dynamically from the [FakeStore API](https://fakestoreapi.com/)
  - Displays name, price, category, image, and rating

- **Shopping Cart:**
  - Add/remove products from the cart
  - View total price and item summary

- **Payment Integration:**
  - Stripe Checkout integration for secure payments
  - Handles payment confirmation and success screen

- **Persistence:**
  - MySQL database to store user information
  - SQLAlchemy ORM for database access

- **Security:**
  - Passwords are securely hashed using Werkzeug
  - Environment setup allows for secret key and API keys protection

---

## Prerequisites

- Python 3.x
- MySQL Server
- Stripe account (for payment API keys)

### Required Python Packages:

- `flask`
- `flask_sqlalchemy`
- `flask_login`
- `stripe`
- `requests`

---

## Installation

1. **Clone this repository**:

```bash
git clone https://github.com/your-username/flask-ecommerce-stripe.git
cd flask-ecommerce-stripe
Create a virtual environment and activate it:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up your MySQL Database:

Create a database named flask_app_db1

Update the SQLALCHEMY_DATABASE_URI in app.py with your credentials:

python
Copy
Edit
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/flask_app_db1'
Initialize the database:

bash
Copy
Edit
python
>>> from app import db
>>> db.create_all()
>>> exit()
Set your Stripe API Keys:

Get your Publishable and Secret keys from Stripe dashboard

Replace them in app.py:

python
Copy
Edit
stripe.api_key = 'sk_test_...'  # Your Stripe Secret Key
Set your Flask secret key:

python
Copy
Edit
app.config['SECRET_KEY'] = 'your_flask_secret_key'
Usage
Run the application using:

bash
Copy
Edit
python app.py
By default, the app runs on http://localhost:8090.

You can now register, log in, browse products, and test checkout using Stripe test cards (e.g., 4242 4242 4242 4242).

File Structure
php
Copy
Edit
flask-ecommerce-stripe/
│
├── app.py                  # Main Flask app file
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates
│   ├── home.html
│   ├── cart.html
│   ├── checkout.html
│   ├── login.html
│   ├── register.html
│   └── layout.html
│
├── static/                 # CSS/JS/Images
│   └── style.css
│
└── README.md               # Project documentation
How It Works
The app starts by displaying a product catalog fetched from FakeStore API.

Users can register or log in to manage their cart.

When items are added to the cart, they are stored in the user's session.

Upon checkout, the Stripe API processes the payment securely.

After successful payment, the user is redirected to a confirmation page.

Potential Enhancements
Add product search and filtering

Admin dashboard to manage products and orders

Order history for users

Email confirmation after successful checkout

Responsive UI with a framework like Bootstrap or Tailwind CSS

Support for coupons or promo codes

Add product ratings and reviews

Feel free to customize and extend this eCommerce app for your business, portfolio, or hackathon needs!

Created with Flask, SQLAlchemy, Stripe, MySQL, and FakeStore API.

yaml
Copy
Edit

---

Let me know if you’d like a version with screenshots or a `LICENSE` section added too!
