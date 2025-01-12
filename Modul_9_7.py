'''
Функция, которая складывает 3 числа (sum_three)
'''
def sum_three(*nambe):
    return nambe[0] + nambe[1] + nambe[2]
'''
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет 
простым числом и "Составное" в противном случае.
'''
def is_prime(func):
    def new_func(*args):
        n = func(*args)
        lst = [2]
        for i in range(3, n + 1, 2):
            if (i > 10) and (i % 10 == 5):
                continue
            for j in lst:
                if j * j - 1 > i:
                    lst.append(i)
                    break
                if (i % j == 0):
                    break
            else:
                lst.append(i)
        if n == lst[len(lst)-1]:
            print('Простое')
        else:
            print('Составное')
        return n
    return new_func


sum_three = is_prime(sum_three)

result = sum_three(2, 3, 6)
print(result)