from bank import BankAccount

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.accounts = {'checking': BankAccount(), 'savings': BankAccount()}

  def primary_account(self):
    return self.accounts['checking']
  
  def create_account(self, account_type, initial_amount=0):
    self.accounts[account_type] = BankAccount(initial_amount)

  def make_deposit(self, account_type, amount):
    self.accounts[account_type].deposit(amount)
    return self

  def make_withdraw(self, account_type, amount):
    self.accounts[account_type].withdraw(amount)

  def transfer(self, person, amount, account_type):
    if account_type in self.accounts and account_type in person.accounts:
      if self.accounts[account_type].withdraw(amount):
        person.accounts[account_type].deposit(amount)
    else:
      print(f'{account_type} not found')
    return self
  
  def total_funds(self):
    current_balance = 0
    for account_type, account in self.accounts.items():
      current_balance += account.balance
      return current_balance

jack = User('Jack', 'jack@email.com')
jane = User('Jane', 'jane@email.com')
jim = User('Jim', 'jim@email.com')

jack.make_deposit('checking', 1000).make_withdraw('checking', 800)
print(jack.total_funds())
jack.transfer(jane, 100, 'checking')
print(jack.total_funds())
print(jane.total_funds())
# jane.make_deposit(2000).make_deposit(2000).make_deposit(500).make_deposit(500).display_user_balance()

# jim.make_deposit(1000).make_withdraw(500).make_withdraw(200).make_withdraw(400).display_user_balance()

# jack.transfer(jane, 500).display_user_balance().display_user_balance()
