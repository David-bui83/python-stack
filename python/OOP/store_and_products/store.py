from product import Product

class Store:
  def __init__(self, name):
    self.name = name
    self.products = []
  
  def add_product(self, new_product):
    self.products.append(new_product)
    return self

  def sell_product(self, id):
    for prod in self.products:
      if prod.id == id:
        prod.print_info()
        self.products.remove(prod)
    # for i in range(len(self.products)):
    #   if i == id:
    #     self.products[i].print_info()
    #     self.products.remove(self.products[i])
    return self

  def inflation(self,percent_increase):
    # loop through all products
    for product in self.products:
      product.update_price(percent_increase, True)
    #self.products[0].update_price(percent_increase, True)
    return self

  def set_clearance(self, category, percent_discount):
    for product in self.products:
      if product.category == category:
        product.update_price(percent_discount, False)
    # for p in range(len(self.products)):
    #   if self.products[p].category == category:
    #     self.products[p].update_price(percent_discount, False)
    return self

