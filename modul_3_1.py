def count_calls ():   #подсчитывающая вызовы остальных функций.
    global calls
    calls +=1

def string_info(stringInput = '' ):  # принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    count_calls()
    return (len(stringInput),stringInput.upper(),stringInput.lower())

def is_contains(stringInput = '' , listInput = None):  # принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
    count_calls()
    if listInput != None:
        for i in listInput:
            if stringInput.upper() == i.upper():
                return True
    return False

calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)