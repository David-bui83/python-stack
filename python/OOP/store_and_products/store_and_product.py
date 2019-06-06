from store import Store
from product import Product

store1 = Store('Target')
store2 = Store('Walmart')
store3 = Store('Best Buy')

product1 = Product('macbook',1000,'laptop',1)
product2 = Product('mac pro',3000,'desktop',2)
product3 = Product('iphone',1000,'cell phone',3)
product4 = Product('beats',350,'headphone',4)
product5 = Product('ipad',600,'tablet',5)
product6 = Product('xdr',5000,'monitor',6)

print(store1.name)
print(store1.products)
store1.add_product(product1)
store1.add_product(product2)
print(store1.products)
store1.sell_product(1)
print(store1.products)

print(store2.name)
store2.add_product(product3)
store2.add_product(product4)
store2.inflation(.05)
print(store2.products[0].print_info())

print(store3.name)
store3.add_product(product5)
store3.add_product(product6)
store3.set_clearance('monitor', .05)
print(store3.products[1].print_info()) 
