"""
Задача "Записать и запомнить":
"""

def custom_write(file_name: str, strings: list):
    """
    :param file_name: название файла для записи,
    :param strings:  список строк для записи.
    :return:
    Записывать в файл file_name все строки из списка strings, каждая на новой строке.
    Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
    а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell()
    перед записью.
    Пример полученного словаря:
    {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
    Где:    1, 2 - номера записанных строк.
            0, 16 - номера байт, на которых началась запись строк.
            'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.
    """
    nambeLine = 1
    dictFile = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for txtLine in strings:
            nambeByte = file.tell()
            file.write(txtLine+"\n")
            dictFile[(nambeLine,nambeByte)]=txtLine
            nambeLine += 1
    return dictFile

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)