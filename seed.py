from budget_tracker.model import Session, Transaction
from datetime import datetime

def seed_data():
    # Creating a session
    session = Session()

    try:
        # Seed transactions
        transactions = [
            Transaction(amount=100.0, type='income', description='Salary', created_at=datetime.now()),
            Transaction(amount=30.0, type='expense', description='Groceries', created_at=datetime.now()),
            Transaction(amount=50.0, type='income', description='Freelance work', created_at=datetime.now()),
            Transaction(amount=20.0, type='expense', description='Eating out', created_at=datetime.now()),
            Transaction(amount=75.0, type='income', description='Gift', created_at=datetime.now()),
            Transaction(amount=40.0, type='expense', description='Utilities', created_at=datetime.now()),
            Transaction(amount=60.0, type='income', description='Bonus', created_at=datetime.now()),
            Transaction(amount=25.0, type='expense', description='Transportation', created_at=datetime.now()),
            Transaction(amount=90.0, type='income', description='Investment return', created_at=datetime.now()),
            Transaction(amount=35.0, type='expense', description='Entertainment', created_at=datetime.now()),
            
        ]
        # Adding the transactions to the session
        session.add_all(transactions)

        # Committing the changes to the database
        session.commit()

        print("Data seeding successful!")
    except Exception as e:
        print(f"Error seeding data: {e}")
        session.rollback()
    finally:
        # Closing the session
        session.close()

if __name__ == "__main__":
    # Run the data seeding function
    seed_data()
