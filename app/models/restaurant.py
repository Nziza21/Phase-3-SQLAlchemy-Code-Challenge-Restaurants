from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base, Session

class Restaurant(Base):
    __tablename__ = 'restaurants'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    
    reviews = relationship("Review", back_populates="restaurant")

    def get_reviews(self):
        return self.reviews

    def customers(self):
        return [review.customer for review in self.reviews]

    @classmethod
    def fanciest(cls):
        return Session.query(cls).order_by(cls.price.desc()).first()
    
    def all_reviews(self):
        return [review.full_review() for review in self.reviews]