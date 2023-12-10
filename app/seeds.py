from app.models import db, Restaurant, Customer, Review

# Initialize Flask App and SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

# Create instances
restaurant1 = Restaurant(name='Restaurant A', price=3)
restaurant2 = Restaurant(name='Restaurant B', price=2)
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Doe')

# Add instances to session
db.session.add_all([restaurant1, restaurant2, customer1, customer2])
db.session.commit()

# Create reviews
review1 = Review(restaurant=restaurant1, customer=customer1, star_rating=5)
review2 = Review(restaurant=restaurant2, customer=customer1, star_rating=4)
review3 = Review(restaurant=restaurant1, customer=customer2, star_rating=3)

# Add reviews to session
db.session.add_all([review1, review2, review3])
db.session.commit()