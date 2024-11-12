#Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает
# произведение цифр этого числа.
def get_multiplied_digits(number):
    #    for i in str_number:
    #        if int(i) > 0 : result *= int(i)
    #    return result
    if(number > 0):
        str_number = str(number)   # Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
        i = len(str_number)
        if i > 1:
            number = int(str_number[1: i])
            if int(str_number[0]) >0 :
                return int(str_number[0]) * get_multiplied_digits(number)
            else:
                return get_multiplied_digits(number)
        else:
            return int(str_number[0])
    return 1

result = get_multiplied_digits(402030)
print(result)


