class User:
  def __init__(self, name):
    self.name = name
    self.account = 0

  def make_deposit(self, d_amount):
    self.account += d_amount
    return self
  
  def make_withdraw(self, w_amount):
    if w_amount < self.account:
      self.account = self.account - w_amount
      print(self.account)
    else: 
      print('Insufficient fund')
    return self
  def display_user_balance(self):
    print(f"{self.name} balance is {self.account}")
    return self

  def transfer(self, name, amount):
    if amount < self.account:
      self.account -= amount
      name.make_deposit(amount)
    else:
      print('Insufficient fund')
    return self

jack = User('Jack')
jane = User('Jane')
jim = User('Jim')

jack.make_deposit(1000).make_deposit(1000).make_deposit(1000).make_withdraw(500).display_user_balance()

jane.make_deposit(2000).make_deposit(2000).make_deposit(500).make_deposit(500).display_user_balance()

jim.make_deposit(1000).make_withdraw(500).make_withdraw(200).make_withdraw(400).display_user_balance()

jack.transfer(jane, 500).display_user_balance().display_user_balance()
