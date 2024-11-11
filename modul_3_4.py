

#1 Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
def single_root_words(root_word, *other_word):
    same_words = []   #2 cоздайте внутри функции пустой список same_words, который пополнится нужными словами.
    for i in other_word: # При помощи цикла for переберите предполагаемо подходящие слова.
        if root_word.lower() in str(i).lower() : #слов списка other_words, которые содержат root_word
             same_words.append(i)
        if str(i).lower() in root_word.lower() : # аоборот root_word содержит одно из этих слов.
             same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)