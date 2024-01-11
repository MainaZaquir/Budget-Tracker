import unittest
import argparse
from unittest.mock import patch
from io import StringIO
from budget_tracker.cli.cli import parse_args, add_transaction_command, balance_command

class TestCLI(unittest.TestCase):
    def test_parse_args_add_transaction(self):
        args = ['add-transaction', '--amount', '100', '--type', 'income', '--description', 'Salary']
        parsed_args = parse_args(args)
        self.assertEqual(parsed_args.command, 'add-transaction')
        self.assertEqual(parsed_args.amount, 100)
        self.assertEqual(parsed_args.type, 'income')
        self.assertEqual(parsed_args.description, 'Salary')

    def test_parse_args_balance(self):
        args = ['balance']
        parsed_args = parse_args(args)
        self.assertEqual(parsed_args.command, 'balance')

    @patch('sys.stdout', new_callable=StringIO)
    def test_add_transaction_command(self, mock_stdout):
        args = argparse.Namespace(amount=100, type='income', description='Salary')
        add_transaction_command(args)
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "Your transaction added successfully!")

    @patch('sys.stdout', new_callable=StringIO)
    def test_balance_command(self, mock_stdout):
        balance_command(None)
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output.startswith("Your current balance is:"))

if __name__ == '__main__':
    unittest.main()
