# 🛍️ Flask eCommerce Web App

This project is a Python-based eCommerce web application built using **Flask** that allows users to register, log in, browse products from a third-party API, manage a shopping cart, and make secure payments using **Stripe**. It uses **MySQL** as the backend database and includes features like session handling, password hashing, and responsive user experience.

---

## Features

- **User Management:**
  - User registration and login
  - Secure password hashing using Werkzeug
  - Session-based login management with Flask-Login

- **Product Catalog:**
  - Fetches products from [FakeStore API](https://fakestoreapi.com/)
  - Displays product title, price, image, category, and rating

- **Shopping Cart:**
  - Add and remove items from the cart
  - Displays cart total and item list

- **Payment Integration:**
  - Secure payment processing via **Stripe Checkout**
  - Stripe API used to create sessions and handle payments

- **Persistence:**
  - MySQL database to store registered users
  - SQLAlchemy ORM for database interaction

- **Security:**
  - Secure secret key for session encryption
  - Stripe secret and publishable keys hidden in backend config

---

## Prerequisites

- Python 3.x
- MySQL server installed and running
- Stripe account for API keys

### Required Python Packages

- `flask`
- `flask_sqlalchemy`
- `flask_login`
- `stripe`
- `requests`

---

## Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/your-username/flask-ecommerce-stripe.git
   cd flask-ecommerce-stripe
   ```

2. **Create and activate virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MySQL database:**

   - Create a MySQL database named `flask_app_db1`
   - Update the database URI in `app.py`:

     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://your_user:your_password@localhost/flask_app_db1'
     ```

5. **Initialize the database:**

   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

6. **Configure Stripe Keys and Flask Secret:**

   In `app.py`, set the keys:

   ```python
   stripe.api_key = 'sk_test_your_stripe_secret_key'
   app.config['SECRET_KEY'] = 'your_flask_secret_key'
   ```

---

## Usage

Run the app using:

```bash
python app.py
```

By default, the app runs on `http://localhost:8090`.

Visit the URL in your browser to:

- Register a new user
- Log in and browse products
- Add products to cart
- Checkout using Stripe test cards (e.g. `4242 4242 4242 4242`)

---

## File Structure

```
flask-ecommerce-stripe/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Dependencies list
├── templates/              # HTML templates
│   ├── home.html
│   ├── cart.html
│   ├── checkout.html
│   ├── login.html
│   ├── register.html
│   └── layout.html
│
├── static/                 # Static assets (CSS/images)
│   └── style.css
│
└── README.md               # Project documentation
```

---

## How It Works

1. The app loads products from the FakeStore API.
2. Users register and log in using a secure system.
3. Products can be added to a cart managed via Flask sessions.
4. On checkout, Stripe Checkout is used for processing payments.
5. After payment, users are redirected to a success page.

---

## Potential Enhancements

- Admin panel for managing products and orders
- Product search and filter features
- Order history and receipts for users
- Email confirmation after payment
- Responsive UI with Bootstrap or Tailwind CSS
- Support for coupons and promo codes
- Image optimization and performance enhancements

---

Feel free to enhance and adapt this eCommerce platform for your personal projects, hackathons, or small business!

---

*Built with Flask, SQLAlchemy, MySQL, Stripe, and FakeStore API.*
