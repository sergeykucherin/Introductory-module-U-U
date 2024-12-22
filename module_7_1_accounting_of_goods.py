class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        file = open(self.__file_name, 'a+')
        file.seek(0)
        if file.readable() or file.tell() != 0:
            file = open(self.__file_name, 'r')
            file.close()
        else:
            file = open(self.__file_name, 'w')
            file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        current_products = self.get_products().splitlines()  # Получаем текущие строки
        current_product_names = [line.split(",")[0].strip() for line in current_products]  # Имена продуктов
        for product in products:
            if product.name in current_product_names:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(str(product) + '\n')
                file.close()  # Выводим информацию о добавленном продукте

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())

