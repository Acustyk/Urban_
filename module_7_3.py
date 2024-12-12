"""
Задача "Найдёт везде":
Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать
их в атрибут file_names в виде списка или кортежа.

Алгоритм получения словаря такого вида в методе get_all_words:
Создайте пустой словарь all_words.
Переберите названия файлов и открывайте каждый из них, используя оператор with.
Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.

find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().
for name, words in get_all_words().items():
  # Логика методов find или count
"""
class WordsFinder:
    def __init__(self, *listFileName):
        self.file_names = []
        for i in listFileName:
            self.file_names.append(i)

    def get_all_words(self):
        """- подготовительный метод, который возвращает словарь следующего  вида:
    {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
    Где: 'file1.txt', 'file2.txt', '' file3.txt '' - названия файлов.
    ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
        """
        zn = [',', '.', '=', '!', '?', ';', ':', ' - ','\n']
        dictFile = {}
        for nameFile in self.file_names:
            with open(nameFile,'r', encoding='utf-8') as file:
                txt = file.read()
                for i in zn:
                    txt = txt.replace(i,' ')
                i=0
                lenTxt= txt.__len__()
                txtList = []
                while i < lenTxt:
                    j=txt.find(' ',i)
                    if i != j:
                        txtList.append(txt[i:j])
                    i = j + 1
                dictFile.update({nameFile:txtList})
        return dictFile

    def count(self, word):
        """
        :param word: - искомое слово.
        :return: Возвращает словарь, где ключ - название файла, значение - количество слов word в
        списке слов этого файла.
        """
        newDict = {}
        txtDict = self.get_all_words()
        word = word.lower()
        for k, v in txtDict.items():
            indices = [index for index, element in enumerate(v) if element.lower() == word]
            newDict[k] = indices.__len__()
        return newDict

    def find(self, word: str):
        """
        :param word: - искомое слово
        :return: словарь, где ключ - название файла, значение - позиция первого такого слова в
        списке слов этого файла.
        """
        newDict={}
        txtDict = self.get_all_words()
        word = word.lower()
        for k, v in txtDict.items():
            indices = [index for index, element in enumerate(v) if element.lower() == word]
            newDict[k]=indices[0]+1
        return newDict


info = [
    "It's a text for task Найти везде,",
    "Используйте его для самопроверки.",
    "Успехов в решении задачи!",
    "text text text"
    ]
file=open('test_file.txt','w', encoding='utf-8')
for txtLine in info:
    file.write(txtLine + "\n")
file.close()

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

