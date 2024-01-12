from budget_tracker.database import Session, Transaction
from sqlalchemy import func
from budget_tracker.database import Session, Transaction

def add_transaction(amount, transaction_type, description=None):
    session = Session()

    try:
        new_transaction = Transaction(amount=amount, type=transaction_type, description=description)
        session.add(new_transaction)
        session.commit()
        print("Your transaction added successfully!")
    except Exception as e:
        print(f"Error adding transaction: {e}")
        session.rollback()
    finally:
        session.close()

def get_balance():
    session = Session()

    total_income = session.query(func.sum(Transaction.amount)).filter_by(type='income').scalar() or 0
    total_expenses = session.query(func.sum(Transaction.amount)).filter_by(type='expense').scalar() or 0

    session.close()
    return total_income - total_expenses

def get_transactions():
    session = Session()
    transactions = session.query(Transaction).all()
    session.close()
    return transactions
