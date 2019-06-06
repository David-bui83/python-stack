class Product:
  def __init__(self, name, price, category, id):
    self.name = name
    self.price = price 
    self.category = category
    self.id = id
  
  def update_price(self, percent_change, is_increased):

    new_amount = self.price * percent_change
    if is_increased:
      self.price += new_amount
    else:
      self.price -= new_amount

    return self

  def print_info(self):
    print(f'Product: {self.name} | Category: {self.category} | Price: {self.price}')

  def __repr__(self):
    return f'Product: {self.name} | Category: {self.category} | Price: {self.price}'    

# new_p = Product('bike', 50, 'outdoor')
# new_p.print_info()
# new_p.update_price(.05, True)
# new_p.print_info()