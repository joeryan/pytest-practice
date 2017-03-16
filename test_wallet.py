# test_wallet.py

import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def empty_wallet():
  '''Returns a wallet with balance = 0
  '''
  return Wallet()

@pytest.fixture
def wallet():
  '''Returns a wallet with balance = 20
  '''
  return Wallet(20)

def test_default_initial_amount(empty_wallet):
  assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
  assert wallet.balance == 20 

def test_wallet_add_cash(wallet):
  wallet.add_cash(100)
  assert wallet.balance == 120 

def test_wallet_spend_cash(wallet):
  wallet.spend_cash(10)
  assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(wallet):
  with pytest.raises(InsufficientAmount):
    wallet.spend_cash(30)

@pytest.mark.parametrize("earned,spent,expected", [
  (30, 10, 20),
  (20, 2, 18),
])
def test_transactions(earned, spent, expected):
  wallet = empty_wallet()
  wallet.add_cash(earned)
  wallet.spend_cash(spent)
  assert wallet.balance == expected
