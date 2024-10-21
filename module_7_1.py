from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name},  {self.weight},  {self.category}'


class Shop(Product):
    def __init__(self, name, weight, category, __file_name = 'Goods.txt'):
        super().__init__(name, weight, category)
        self.__file_name = __file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        goods = file.read()
        file.close()
        return str(goods)

    def add(self, *products):
        for product in products:
            string =  str(product)
            file = open(self.__file_name, 'r')
            goods = file.read()
            file.close()
            if string in goods:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'\n {string}')
                file.close()


s1 = Shop(' ',  0, ' ')
p1 = Product('Potato', 50.5, 'vegetables')
p2 = Product('Spaghetti', 3.5, 'groceries')
p3 = Product('Potato', 5.5, 'vegetables')
print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

