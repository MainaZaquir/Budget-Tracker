import argparse
import sys
import click
from datetime import datetime
from budget_tracker.tracker import add_transaction, get_balance

def add_transaction_command(args):
    description = args.description
    amount = args.amount
    date = args.date

    if not date:
        date = datetime.now()

    transaction = {
        'description': description,
        'amount': amount,
        'date': date,
    }

    add_transaction(transaction)

    click.echo(f"Added transaction: {transaction['description']} for ${transaction['amount']} on {transaction['date']}")

def balance_command(args):
    balance = get_balance()
    click.echo(f"Your current balance is: ${balance}")

def interactive_mode():
    click.echo("Welcome to Budget Tracker CLI!")

    while True:
        click.echo("Please enter your command")
        user_input = click.prompt("budget_tracker >")

        if user_input == "exit":
            break
        elif user_input == "add_transaction":
            add_transaction_command()
        elif user_input == "balance":
            balance_command()
        else:
            click.echo("Invalid command. Please try again.")

def parse_args(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description="Budget Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_transaction_parser = subparsers.add_parser(
        "add_transaction",
        description="Add a new transaction",
    )
    add_transaction_parser.add_argument(
        "--description", required=True, help="Description of the transaction"
    )
    add_transaction_parser.add_argument(
        "--amount", type=float, required=True, help="Amount of the transaction"
    )
    add_transaction_parser.add_argument(
        "--date", help="Date of the transaction in YYYY-MM-DD format"
    )
    add_transaction_parser.set_defaults(func=add_transaction_command)

    balance_parser = subparsers.add_parser(
        "balance",
        description="Get the current balance",
    )
    balance_parser.set_defaults(func=balance_command)

    interactive_mode()

if __name__ == "__main__":
    parse_args()


# python cli.py add_transaction --description "Transaction Description" --amount 50 --date "2024-01-15"
# python cli.py balance
# python cli.py

