from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime  # Add this import

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    description = Column(String)
    timestamp = Column(DateTime, server_default=func.now())
    created_at = Column(DateTime, default=func.now())  # Corrected default value

engine = create_engine('sqlite:///budget_tracker.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()