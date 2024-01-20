# Budget Tracker CLI

Welcome to the Budget Tracker CLI! This command-line application helps you manage and track your budget with ease.

## Overview

The Budget Tracker CLI allows users to add income and expenses, view transactions, and check their budget balance.

## Installation

To use the Budget Tracker CLI, follow these steps:

1. Install [Python](https://www.python.org/downloads/) (if not already installed).
2. Clone this repository:
   ```bash
   `git clone https://github.com/yourusername/Budget-Tracker.git`
   `cd budget-tracker-cli`
3. Set up a virtual environment and install dependencies:
    ` pipenv install`

## Usage

To use the Budget Tracker CLI, run the main.py script with appropriate commands. Here are some examples:

Copy the codes and run them in your virtual environment

# To add an income transaction
`python main.py add-income 500 "Salary"`

# To add an expense transaction
`python main.py add-expense 50 "Groceries"`

# To view all your transactions
`python main.py view-transactions`

# To check your budget balance
`python main.py check-balance`

## Database

This application uses SQLAlchemy and Alembic for database management. To set up the database, run the following commands:

Copy the following code
# To create initial migrations
  `alembic revision --autogenerate -m "Initial migration"  `
  `alembic upgrade head`

## Running Tests

To run tests, use the following command:

Copy the following code
  `pytest`
  
## Contributing
If you'd like to contribute to the project, please follow these guidelines:

    1. Check the issues for existing tasks.
    2. Fork the repository and create a new branch for your contribution.
    3. Submit a pull request with a clear description of your changes.

## Credits

This application was created by [Maina Zaquir](https://github.com/MainaZaquir). [Caleb Kiprotich](https://github.com/Calebbii) for providing the guidance and support necessary for developing this application.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
