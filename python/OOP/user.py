class User:
  def __init__(self, name):
    self.name = name
    self.account = 0

  def make_deposit(self, d_amount):
    self.account += d_amount
  
  def make_withdraw(self, w_amount):
    if w_amount < self.account:
      self.account = self.account - w_amount
      print(self.account)
    else: 
      print('Insufficient fund')

  def display_user_balance(self):
    print(f"{self.name} balance is {self.account}")

  def transfer(self, name, amount):
    if amount < self.account:
      self.account -= amount
      name.make_deposit(amount)

    else:
      print('Insufficient fund')

jack = User('Jack')
jane = User('Jane')
jim = User('Jim')

jack.make_deposit(1000)
jack.make_deposit(1000)
jack.make_deposit(1000)
jack.make_withdraw(500)
jack.display_user_balance()

jane.make_deposit(2000)
jane.make_deposit(2000)
jane.make_deposit(500)
jane.make_deposit(500)
jane.display_user_balance()

jim.make_deposit(1000)
jim.make_withdraw(500)
jim.make_withdraw(200)
jim.make_withdraw(400)
jim.display_user_balance()

jack.transfer(jane, 500)
jack.display_user_balance()
jane.display_user_balance()
