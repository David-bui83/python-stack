class BankAccount:
  def __init__(self, int_rate=0.04, balance=0):
    self.int_rate = int_rate
    self.balance = balance
  
  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
    return self

  def withdraw(self, amount):
    if amount < self.balance:
      self.balance -= amount
      return self
    print('Insufficient fund')
    return self

  def display_account_info(self):
    print(self.balance)
    return self

  def yield_interest(self):
    interest_accumulated = self.int_rate * self.balance
    self.balance += interest_accumulated
    return self


account1 = BankAccount()
account2 = BankAccount()

account1.deposit(1000).deposit(1000).deposit(1000).withdraw(200).yield_interest().display_account_info()

account2.deposit(1000).deposit(1000).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()