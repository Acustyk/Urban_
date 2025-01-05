
first = 'Мама мыла раму'
second = 'Рамена мало было'
'''
Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
Здесь ? - место написания lambda-функции.
'''
comparison_ = list(map(lambda x, y: x==y , first, second))
'''
Результатом должен быть список совпадения букв в той же позиции:
[False, True, True, False, False, False, False, False, True, False, False, False, False, False]
Где True - совпало, False - не совпало.
'''
print(comparison_)


'''
Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр 
принимающий неограниченное количество данных любого типа.
Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в 
том же виде.
Функция get_advanced_writer возвращает функцию write_everything.
'''
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        def str_x(x):
            types_data = str(type(x))
            if 'str' in types_data or 'float' in types_data:
                return ' ' + x
            if 'int' in types_data:
                return ' ' +  str(x)
            if 'dict' in types_data:
                str_ = str_x(list(x.keys()))
                return str_ + str_x(list(x.values()))
            if 'list' in types_data or 'tuple' in types_data or 'set' in types_data:
                str_ = ''
                for y in x:
                    str_ += str_x(y)
                return str_
        with open(file_name, 'w', encoding='utf-8') as file:
            for x in data_set:
                file.write(str_x(x))
    return write_everything



write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке',7.0])




'''
Метод __call__:
Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
В этом классе также определите метод __call__ который будет случайным образом выбирать слово 
из words и возвращать его. Для случайного выбора с одинаковой вероятностью для каждого данного 
в коллекции можете использовать функцию choice из модуля random.
'''






#from random import choice

# Ваш класс здесь

#first_ball = MysticBall('Да', 'Нет', 'Наверное')

#print(first_ball())
#print(first_ball())
#print(first_ball())