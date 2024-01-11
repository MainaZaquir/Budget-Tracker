from budget_tracker.tracker import add_transaction, get_balance
from budget_tracker.cli.cli import interactive_mode, parse_args, add_transaction_command, balance_command

def main():
    args = parse_args()

    if hasattr(args, 'func'):
        if args.func == add_transaction_command:
            args.func(args, add_transaction)
        elif args.func == balance_command:
            args.func(args, get_balance)
    else:
        interactive_mode()

if __name__ == "__main__":
    main()
