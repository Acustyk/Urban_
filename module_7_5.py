import os
import time

"""
Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
Примените os.path.join для формирования полного пути к файлам.
Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
Используйте os.path.getsize для получения размера файла.
Используйте os.path.dirname для получения родительской директории файла.

formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
 """
cuгrentDir = os.getcwd() # текущая директория
print(cuгrentDir)
for root, dirs, files in os.walk(cuгrentDir):
    print(f"Текущая директория '{root}' содержит: ")
    print(f"    - подкаталогов {"нет" if dirs.__len__() == 0 else dirs.__len__()}.")
    print(f"    - файлов {"нет" if files.__len__() == 0 else files.__len__() }.")
    for fil in files:
        print(f"       {fil}, путь: {os.path.join(root,fil)}, ")
        print(f"              Размер: {os.path.getsize(fil)} байт, Время изменения: {time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(fil)))}")
