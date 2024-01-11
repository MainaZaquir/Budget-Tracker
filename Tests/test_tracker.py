import unittest
from budget_tracker.tracker import add_transaction, get_balance, get_transactions
from budget_tracker.database import Session, Transaction

class TestTracker(unittest.TestCase):
    def test_add_transaction(self):
        add_transaction(150, 'income', 'Freelance Job')

        session = Session()
        retrieved_transaction = session.query(Transaction).filter_by(description='Freelance Job').first()
        self.assertIsNotNone(retrieved_transaction)
        self.assertEqual(retrieved_transaction.amount, 150)
        self.assertEqual(retrieved_transaction.type, 'income')
        self.assertEqual(retrieved_transaction.description, 'Freelance Job')

        session.rollback()
        session.close()

    def test_get_balance(self):
        add_transaction(1000, 'income', 'Salary')
        add_transaction(300, 'expense', 'Groceries')
        add_transaction(50, 'expense', 'Dinner')

        balance = get_balance()
        self.assertEqual(balance, 650)

    def test_get_transactions(self):
        add_transaction(200, 'income', 'Side Job')

        transactions = get_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].amount, 200)
        self.assertEqual(transactions[0].type, 'income')
        self.assertEqual(transactions[0].description, 'Side Job')
