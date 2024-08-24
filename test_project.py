import pytest
from project import load_data, save_data, create_account, deposit, withdraw, check_balance, transaction_history, delete_account

def test_create_account():
    save_data({})
    create_account("123456", "John Doe", 100.0)
    data = load_data()
    assert "123456" in data, "Account creation failed."
    assert data["123456"]["balance"] == 100.0, "Initial deposit incorrect."

def test_deposit():
    save_data({})
    create_account("123456", "John Doe", 100.0)
    deposit("123456", 50.0)
    data = load_data()
    assert data["123456"]["balance"] == 150.0, "Deposit failed."

def test_withdraw():
    save_data({})
    create_account("123456", "John Doe", 100.0)
    withdraw("123456", 50.0)
    data = load_data()
    assert data["123456"]["balance"] == 50.0, "Withdrawal failed."

def test_check_balance(capsys):
    save_data({})
    create_account("123456", "John Doe", 100.0)
    check_balance("123456")
    captured = capsys.readouterr()
    assert "100.0" in captured.out, "Balance check failed."

def test_transaction_history(capsys):
    save_data({})
    create_account("123456", "John Doe", 100.0)
    deposit("123456", 50.0)
    withdraw("123456", 30.0)
    transaction_history("123456")
    captured = capsys.readouterr()
    assert "deposit" in captured.out and "withdrawal" in captured.out, "Transaction history failed."

def test_delete_account():
    save_data({})
    create_account("123456", "John Doe", 100.0)
    delete_account("123456")
    data = load_data()
    assert "123456" not in data, "Account deletion failed."

if __name__ == "__main__":
    pytest.main()
