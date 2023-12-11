# app/main.py
from sqlalchemy.orm import Session
from app.config import SessionLocal
from app.seeds import seed_data
from app.models.restaurant import Restaurant
from app.models.customer import Customer
from app.models.review import Review

# Initialize database
db = SessionLocal()
seed_data(db)

# Example queries
restaurant = db.query(Restaurant).filter_by(name="Restaurant A").first()
print(restaurant.reviews)

customer = db.query(Customer).filter_by(first_name="John").first()
print(customer.restaurants)

# Additional methods testing
fanciest_restaurant = Restaurant.fanciest(db)
print(f"Fanciest Restaurant: {fanciest_restaurant.name}")

# Retrieving the review_1 instance
review_1 = seed_data(db)
full_review = review_1.full_review()
print(full_review)