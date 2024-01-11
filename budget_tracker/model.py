from sqlalchemy import Column, Integer, Float, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    type = Column(String(10), nullable=False)
    description = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# Add more models as needed

# Creating a SQLite database engine
DATABASE_URL = "sqlite:///budget_tracker.db"
engine = create_engine(DATABASE_URL)

# Creating tables in the database
Base.metadata.create_all(bind=engine)

# Creating a session factory
Session = sessionmaker(bind=engine)
