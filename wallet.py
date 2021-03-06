# wallet.py
# simple wallet that allows adding and spending cash

class InsufficientAmount(Exception):
  pass

class NegativeTransaction(Exception):
  pass

class Wallet():

  def __init__(self, amount = 0):
    self.balance = amount 

  def add_cash(self, deposit):
    if deposit < 0:
      raise NegativeTransaction("Transaction Amount {0} cannot be negative.".format(deposit))
    self.balance += deposit

  def spend_cash(self, spend_amount):
    if spend_amount < 0:
      raise NegativeTransaction("Transaction Amount {0} cannot be negative.".format(spend_amount))
    if self.balance - spend_amount < 0:
      raise InsufficientAmount("Not enough available to spend {0}".format(spend_amount))
    if spend_amount > 0:
      self.balance -= spend_amount
    else:
      print("cannot be a negative amount")


