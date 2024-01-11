import argparse
from budget_tracker.tracker import add_transaction, get_balance

def add_transaction_command(args):
    add_transaction(args.amount, args.type, args.description)

def balance_command(args):
    balance = get_balance()
    print(f"Your current balance is: {balance}")

def interactive_mode():
    while True:
        command = input("Enter a command (add-transaction, balance, exit): ").strip().lower()

        if command == 'add-transaction':
            amount = float(input("Enter the transaction amount: "))
            transaction_type = input("Enter the transaction type (income/expense): ")
            description = input("Enter a description (optional): ")
            add_transaction(amount, transaction_type, description)

        elif command == 'balance':
            balance_command(None)

        elif command == 'exit':
            break

        else:
            print("Invalid command. Try again.")

def parse_args():
    parser = argparse.ArgumentParser(description='Budget Tracker CLI')
    
    subparsers = parser.add_subparsers(title='commands', dest='command')

    # Add Transaction Command
    add_transaction_parser = subparsers.add_parser('add-transaction', help='Add a new transaction')
    add_transaction_parser.add_argument('--amount', type=float, required=True, help='Transaction amount')
    add_transaction_parser.add_argument('--type', choices=['income', 'expense'], required=True, help='Transaction type')
    add_transaction_parser.add_argument('--description', help='Transaction description')
    add_transaction_parser.set_defaults(func=add_transaction_command)

    # Balance Command
    balance_parser = subparsers.add_parser('balance', help='Get current balance')
    balance_parser.set_defaults(func=balance_command)

    return parser.parse_args()

def main():
    args = parse_args()
    
    if hasattr(args, 'func'):
        args.func(args)
    else:
        interactive_mode()

if __name__ == "__main__":
    main()
