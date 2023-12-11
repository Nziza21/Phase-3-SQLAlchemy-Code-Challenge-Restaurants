from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

# Replace 'DATABASE_URL' with your actual database URL
engine = create_engine('DATABASE_URL')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# Your testing code here
# For example:
customer = session.query(Customer).first()
restaurant = session.query(Restaurant).first()

print(customer.full_name())
print(customer.favorite_restaurant().name)

# Add a review and check if it was added
customer.add_review(restaurant, 4)
print(customer.reviews)

# Delete reviews and check if they were removed
customer.delete_reviews(restaurant)
print(customer.reviews)

# Test fanciest() and all_reviews()
fanciest_restaurant = Restaurant.fanciest()
print(f"Fanciest restaurant: {fanciest_restaurant.name}")
print(f"All reviews for the fanciest restaurant: {fanciest_restaurant.all_reviews()}")