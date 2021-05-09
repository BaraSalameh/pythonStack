class Store:
    def __init__(self,name,products= []):
        self.name = name
        self.products = products

    def add_product(self, new_product):
        flag = 0
        for i in range(len(self.products)):
            if new_product.id == self.products[i].id:
                print("This product is already added")
                flag += 1
        if flag == 0:
            self.products.append(new_product)
        return self
    
    def sell_product(self, id):
        for i in range(0,len(self.products)):
            if self.products[i].id == id:
                print("product soled successfully, product info {}".format(self.products[i].print_info()))
                self.products.pop(i)
                break
        return self
    
    def inflation(self, percent_increase):
        for i in self.products:
            i.update_price(percent_increase,True)

    def set_clearance(self, category, percent_discount):
        for i in self.products:
            if i.category == category:
                i.update_price(percent_discount,False)

