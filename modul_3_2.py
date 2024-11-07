def send_email ( messege_ = '', recipient = '', sender = "university.help@gmail.com"):
#  Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
    lenStr = len(recipient)
    if (recipient.find("@") < 1 #  до знака "@" есть хотя бы один символ
            or not( not recipient.find(".com",lenStr-4,lenStr) < 0
            or not recipient.find(".ru",lenStr-3,lenStr) < 0
            or not recipient.find(".net",lenStr-4,lenStr) < 0)):
        print("1 Невозможно отправить письмо с адреса ",sender," на адрес ",recipient)
        return
    lenStr = len(sender)
    if (sender.find("@") < 1                                #  до знака "@" есть хотя бы один символ
        or not( not sender.find(".com", lenStr - 4, lenStr) < 0
        or not sender.find(".ru", lenStr - 3, lenStr) < 0
        or not sender.find(".net", lenStr - 4, lenStr) < 0)):
        print("Невозможно отправить письмо с адреса ",sender," на адрес ",recipient)
        return #  то вывести в консоль строку:
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса ",sender," на адрес ",recipient,".")
        return
    print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ",sender," на адрес ",recipient,".")
# Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
# В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')