def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)  # Функция должна выводить входные параметры

print_params(b = 25)
print_params(c = [1,2,3])

values_list =[5,"ok",False] #с тремя элементами разных типов.
values_dict = {'a': 3,'b': 'path', 'c': False} #с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
print_params(*values_list)     # Передайте values_list и values_dict в функцию print_params,
print_params(**values_dict)    # используя распаковку параметров (* для списка и ** для словаря).

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)