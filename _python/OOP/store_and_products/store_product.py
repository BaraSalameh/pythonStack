import product
import store

#  creating objects
print("creating objects")

bara = store.Store("Bara Salameh")
tShirt = product.Products(8,"t-shirt",15,"upperCromby")
trowser = product.Products(32,"trowser",30,"TommyJeans")

tShirt.print_info()
trowser.print_info()

print("_"*30)

#  adding products and updating product prices
print("adding products and updating product prices")

bara.add_product(tShirt).add_product(trowser)

print("updating tShirt by 0.05 price")
tShirt.update_price(0.05,True).print_info()

print("updating trowser by 0.01 price")
trowser.update_price(0.01,True).print_info()

print("_"*30)

#  testing the inflation method
print("testing the inflation method")

print("inflation by 0.05")
bara.inflation(0.05)
tShirt.print_info()
trowser.print_info()

print("_"*30)

# testing the set_clearance method
print("testing the set_clearance method")

print("set clearance for category TommyJeans by 0.5")
bara.set_clearance("TommyJeans",0.5)
trowser.print_info()

print("set clearance for category upperCromby by 0.1")
bara.set_clearance("upperCromby",0.1)
tShirt.print_info()

print("_"*30)

# testing the sell product with id method
print("testing the sell product with id method")

print("sell product with id = 8 (tShirt)")
bara.sell_product(8)

print("sell product with id = 32 (trowser)")
bara.sell_product(32)

print("_"*30)




