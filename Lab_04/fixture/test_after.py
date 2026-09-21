import pytest
from bank import BankAccount

@pytest.fixture
def account():
    return BankAccount(100)

def test_deposit(account):
    account.deposit
    assert account.balance == 150

def test_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70