def apply_all_func(int_list, *functions):
    """
    Вызвать каждую функцию к переданному списку int_list

    :param int_list: - список из чисел (int, float)
    :param functions: - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
    :return: словарь, где ключом будет название вызванной функции,
               а значением - её результат работы со списком int_list.
    """
    results ={} #создайте пустой словарь .
    try:
        for func_ in functions: #Переберите все функции из *functions.
            results[func_.__name__]=func_(int_list)
        return results
    except TypeError :
        print('В numbers записан некорректный тип данных')
        return None
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

