class Product:
    def __init__(self,product_id,name,price,stock):
        self.product_id = product_id
        self.name =name
        self.price = price
        self.stock =stock

    def create_product(self,product_id,name,price,stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        print(f"product{self.name}created !")

    def read_product(self):
        return f"product id : {self.product_id},name:{self.name},price:{self.price},stock:{self.stock}"


    def update_product(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

        print(f"product{self.product_id}updated")

    def delete_product(self):
        print(f"product{self.product_id} deleted  ")

class ProductManager:
    def __init__(self):
        self.products = {}


    def add_product(self, product):
        self.products[product.product_id] = product
        print(f"Product {product.name} added to the system.")


    def get_product(self, product_id):
        if product_id in self.products:
            return self.products[product_id].read_product()
        else:
            return f"Product with ID {product_id} not found."


    def update_product_in_system(self, product_id, name, price, stock):
        if product_id in self.products:
            self.products[product_id].update_product(name, price, stock)
        else:
            print(f"Product with ID {product_id} not found.")


    def delete_product_from_system(self, product_id):
        if product_id in self.products:
            self.products[product_id].delete_product()
            del self.products[product_id]
        else:
            print(f"Product with ID {product_id} not found.")



product1=Product(122,"cahara",345,4)
product2=Product(234,"dhwwje",374,8)

product2.create_product(123,"charan",8478,7)
product2.read_product()
prodcut3=product2.update_product("charan",4878,29)
Product.delete_product(product1)




