# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'  # Adjust based on your database choice
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'