import unittest
from budget_tracker.database import Transaction, Session

class TestDatabase(unittest.TestCase):
    def test_create_transaction(self):
        session = Session()

        new_transaction = Transaction(amount=100, type='income', description='Salary')
        session.add(new_transaction)
        session.commit()

        retrieved_transaction = session.query(Transaction).filter_by(description='Salary').first()

        self.assertEqual(retrieved_transaction.amount, 100)
        self.assertEqual(retrieved_transaction.type, 'income')
        self.assertEqual(retrieved_transaction.description, 'Salary')

        session.rollback()
        session.close()

    def test_get_transactions(self):
        session = Session()

        transactions_before = session.query(Transaction).all()
        self.assertEqual(len(transactions_before), 0)

        new_transaction = Transaction(amount=200, type='expense', description='Groceries')
        session.add(new_transaction)
        session.commit()

        transactions_after = session.query(Transaction).all()
        self.assertEqual(len(transactions_after), 1)

        session.rollback()
        session.close()
