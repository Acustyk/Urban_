"""Задача "Учёт товаров":
Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables')
и обладать следующими свойствами:
Атрибут name - название продукта (строка).
Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
Атрибут category - категория товара (строка).
Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
Все данные в строке разделены запятой с пробелами.
"""
'''   def __init__(self,name: str,weight: float,category: str):
       self.name = name
       self.weight = weight
       self.category = category
'''
class Product:
    def __init__(self, name: str, weight: float, category: str ):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        t=f'{self.name},{self.weight},{self.category}\n'
        return t
"""
Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
Инкапсулированный атрибут __file_name = 'products.txt'.
Метод get_products(self), который считывает всю информацию из файла __file_name, 
закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
 Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию). 
 Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
"""
class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            txt = file.read()
        return txt

    def add(self,*products):
        with open(self.__file_name, 'r') as file:
            txt = file.read()
        listShop = txt.split()
        fullProducts = []
        for i in listShop:# СОЗДАДИМ СПИСОК ПРОДУКТОВ НА СКЛАДЕ
            listProduct = i.split(',')
            fullProducts.append(Product(listProduct[0], float(listProduct[1]), listProduct[2]))
        for i in products:  # ДОБАВИМ НОВЫЕ
            if  i.name not in txt: # проверка на Имя
                fullProducts.append(i)
                txt += i.__str__()
            else:
                for j in fullProducts:
                    if j.name == i.name :
                        j.weight += i.weight
                        print(f'Продукт {j.name} уже есть в магазине. Итоговый вес {j.weight}.')
        txt = ""
        for i in fullProducts:
            txt += i.__str__()
        with open(self.__file_name, 'w') as file:
            file.write(txt)

#Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())

