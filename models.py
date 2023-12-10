from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def reviews(self):
        return Review.query.filter_by(restaurant_id=self.id).all()

    def customers(self):
        return Customer.query.join(Review).filter(Review.restaurant_id == self.id).all()

    @classmethod
    def fanciest(cls):
        return cls.query.order_by(cls.price.desc()).first()

    def all_reviews(self):
        reviews = Review.query.filter_by(restaurant_id=self.id).all()
        return [review.full_review() for review in reviews]


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)

    def reviews(self):
        return Review.query.filter_by(customer_id=self.id).all()

    def restaurants(self):
        return Restaurant.query.join(Review).filter(Review.customer_id == self.id).all()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        favorite_review = Review.query.filter_by(customer_id=self.id).order_by(Review.star_rating.desc()).first()
        return favorite_review.restaurant if favorite_review else None

    def add_review(self, restaurant, rating):
        review = Review(restaurant=restaurant, customer=self, star_rating=rating)
        db.session.add(review)
        db.session.commit()

    def delete_reviews(self, restaurant):
        reviews = Review.query.filter_by(customer_id=self.id, restaurant_id=restaurant.id).all()
        for review in reviews:
            db.session.delete(review)
        db.session.commit()


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    star_rating = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    restaurant = db.relationship('Restaurant', backref=db.backref('reviews'))
    customer = db.relationship('Customer', backref=db.backref('reviews'))

    def customer(self):
        return Customer.query.get(self.customer_id)

    def restaurant(self):
        return Restaurant.query.get(self.restaurant_id)

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."
