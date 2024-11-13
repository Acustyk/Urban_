
#Для примера, указанного выше, расчёт вёлся следующим образом:
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
level=0

def calculate_structure_sum(data_structure):
    """
   подсчитывает
   Все числа (не важно, являются они ключами или значениям или ещё чем-то).
   Все строки (не важно, являются они ключами или значениям или ещё чем-то)
    """
    summ = 0
    types_data = str(type(data_structure))
    if 'int' in types_data:
        return data_structure
    if 'str' in types_data:
        return len(data_structure)
    if 'dict' in types_data :
        summ += calculate_structure_sum(list(data_structure.keys()))
        return summ + calculate_structure_sum(list(data_structure.values()))
    if  'list' in types_data or 'tuple' in types_data or 'set' in types_data:
        for j in data_structure:
             summ += calculate_structure_sum(j)
        return summ
    return summ


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

