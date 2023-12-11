# app/seeds.py
from sqlalchemy.orm import Session
from app.models.base import Base
from app.models.restaurant import Restaurant
from app.models.customer import Customer
from app.models.review import Review
from app.config import engine

# Create tables
Base.metadata.create_all(bind=engine)

# Sample data
def seed_data(db: Session):
    restaurant_1 = Restaurant(name="Restaurant A", price=3)
    restaurant_2 = Restaurant(name="Restaurant B", price=2)

    customer_1 = Customer(first_name="John", last_name="Doe")
    customer_2 = Customer(first_name="Jane", last_name="Smith")

    review_1 = Review(star_rating=4, restaurant=restaurant_1, customer=customer_1)
    review_2 = Review(star_rating=5, restaurant=restaurant_2, customer=customer_2)

    db.add_all([restaurant_1, restaurant_2, customer_1, customer_2, review_1, review_2])
    db.commit()