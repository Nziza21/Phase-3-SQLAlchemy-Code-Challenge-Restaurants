from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Replace 'DATABASE_URL' with your actual database URL
engine = create_engine('DATABASE_URL')

Session = sessionmaker(bind=engine)
# Remove the global session creation