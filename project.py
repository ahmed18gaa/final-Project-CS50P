import json
import os
from datetime import datetime

DATABASE_FILE = "bank_data.json"

def main():
    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Delete Account")
        print("7. Exit")
        choice = input("Please choose an option: ")

        if choice == '1':
            account_number = input("Enter a new account number: ")
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            create_account(account_number, name, initial_deposit)
        elif choice == '2':
            account_number = input("Enter your account number: ")
            amount = float(input("Enter amount to deposit: "))
            deposit(account_number, amount)
        elif choice == '3':
            account_number = input("Enter your account number: ")
            amount = float(input("Enter amount to withdraw: "))
            withdraw(account_number, amount)
        elif choice == '4':
            account_number = input("Enter your account number: ")
            check_balance(account_number)
        elif choice == '5':
            account_number = input("Enter your account number: ")
            transaction_history(account_number)
        elif choice == '6':
            account_number = input("Enter your account number: ")
            delete_account(account_number)
        elif choice == '7':
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def load_data():
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r") as file:
            return json.load(file)
    else:
        return {}

def save_data(data):
    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file)

def create_account(account_number, name, initial_deposit):
    data = load_data()
    if account_number in data:
        print("Account already exists.")
    else:
        data[account_number] = {
            "name": name,
            "balance": initial_deposit,
            "transactions": [
                {"type": "deposit", "amount": initial_deposit, "date": str(datetime.now())}
            ]
        }
        save_data(data)
        print(f"Account created successfully for {name} with account number {account_number}.")

def deposit(account_number, amount):
    data = load_data()
    if account_number in data:
        data[account_number]["balance"] += amount
        data[account_number]["transactions"].append({"type": "deposit", "amount": amount, "date": str(datetime.now())})
        save_data(data)
        print(f"Successfully deposited {amount}. New balance: {data[account_number]['balance']}")
    else:
        print("Account not found.")

def withdraw(account_number, amount):
    data = load_data()
    if account_number in data:
        if data[account_number]["balance"] >= amount:
            data[account_number]["balance"] -= amount
            data[account_number]["transactions"].append({"type": "withdrawal", "amount": amount, "date": str(datetime.now())})
            save_data(data)
            print(f"Successfully withdrew {amount}. New balance: {data[account_number]['balance']}")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")

def check_balance(account_number):
    data = load_data()
    if account_number in data:
        print(f"Account balance: {data[account_number]['balance']}")
    else:
        print("Account not found.")

def transaction_history(account_number):
    data = load_data()
    if account_number in data:
        print(f"Transaction history for account {account_number}:")
        for transaction in data[account_number]["transactions"]:
            print(f"{transaction['date']}: {transaction['type']} of {transaction['amount']}")
    else:
        print("Account not found.")

def delete_account(account_number):
    data = load_data()
    if account_number in data:
        del data[account_number]
        save_data(data)
        print(f"Account {account_number} has been deleted.")
    else:
        print("Account not found.")

if __name__ == "__main__":
    main()
