# Banking System Console Application

#### Video Demo:  <URL HERE>

## Project Overview

This project is a console-based banking system built with Python. It allows users to create accounts, deposit and withdraw funds, check their account balance, view transaction history, and delete accounts. The project showcases fundamental Python programming concepts such as file handling, data management, and testing.

## Features

- **Account Creation**: Users can create a new account with a unique account number, name, and initial deposit.
- **Deposit**: Users can deposit money into their account, which will update their balance.
- **Withdrawal**: Users can withdraw money from their account, provided they have sufficient funds.
- **Balance Inquiry**: Users can check the balance of their account.
- **Transaction History**: Users can view the history of transactions (deposits and withdrawals) on their account.
- **Account Deletion**: Users can delete their account from the system.

## Project Structure

- **project.py**: The main script that contains the implementation of the banking system, including functions for each feature.
- **test_project.py**: A script containing pytest test cases for the functions in `project.py`.
- **requirements.txt**: A file listing any external libraries required for the project.

## How to Run the Project

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install any required libraries by running:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the project:
    ```bash
    python project.py
    ```

## Testing the Project

To run the tests, simply execute:
```bash
pytest test_project.py
