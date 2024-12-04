from hashlib import sha256
from time import sleep

class User:
    def __init__(self, name : str, passW : str, age_ : int=0) :
        self.nickName_ = name
        self.passWord = sha256(passW.encode())#(в хэшированном виде, число
        self.age = age_
    def __eq__(self, other):
        if isinstance(other, str):
            if other == self.nickName_: return True
        elif isinstance(other, User):
                if other.nickName_ == self.nickName_ and  other.passWord == self.passWord: return True
        return False
    def __str__(self):
        return self.nickName_

class Video:
    def __init__(self, nameVideo: str, longVideo: int, adult_mode: bool=False):
        self.title =  nameVideo           #(заголовок, строка),
        self.duration = longVideo         #(продолжительность, секунды),
        self.time_now = 0                 #(секунда остановки (изначально 0)),
        self.adult_mode = adult_mode #(ограничение по возрасту, bool (False по умолчанию))
    def __eq__(self, other):
        if isinstance(other, str):
            i=other.upper()
            j=self.title.upper()
            if other.upper() in self.title.upper(): return True
        elif isinstance(other, Video):
                i = other.title.upper()
                j = self.title.upper()
                if other.title.upper() in self.title.upper():  return True
        return False

class UrTube:
    def __init__(self):
        self.users = []          #(список объектов User),
        self.videos = []          #(список объектов Video),
        self.current_user = None  #(текущий пользователь, User)
    def getUser(self,nickName: str)-> User :
        for i in self.users:
            if i.nickName_ == nickName:
                return i
    def register(self,nickName: str, password:str, age: int):
        """ добавляет пользователя в список, если пользователя не существует
        (с таким же nickname).
        Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        После регистрации, вход выполняется автоматически.
        """
        if nickName in self.users:
            print("Пользователь {",nickName,"} уже существует")
        else:
            self.current_user = User(nickName,password,age)
            self.users.append(self.current_user)

    def log_in(self,nickName: str, passWord: str):
        """пытается найти пользователя в users с такими же логином и паролем.
        Если такой пользователь существует, то current_user меняется на найденного.
        Помните, что password передаётся в виде строки, а сравнивается по хэшу.
        """
        if nickName in self.users: # пользователь существует надо проверить пароль
            us = User(nickName, passWord)# создаем пользователя для преобразования пароля
            if us in self.users:
                self.current_user = self.getUser(nickName)
        print("Ошибка ввода")
    def log_out(self):
        """    для сброса текущего пользователя на None. """
        self.current_user = None  #(текущий пользователь, User)

    def add(self,*args,**kwargs):
        '''   принимает неограниченное кол-во объектов класса Video
         и все добавляет в videos, если с таким же названием видео ещё не существует.
          В противном случае ничего не происходит.
        '''
        for i in  args :
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self,word: str):
        ''' принимает поисковое слово и возвращает список названий всех видео,
        содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует
        в строке 'Urban the best' (не учитывать регистр).
        '''
        newList = []
        for i in self.videos:
            if word == i:
                newList.append(i.title)
        return newList

    def watch_video(self,title: str):
        '''принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится,
         если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
         После текущее время просмотра данного видео сбрасывается.
        '''
        if self.current_user == None :
            print ("Войдите в аккаунт, чтобы смотреть видео")
            return
        for i in self.videos:
            if title == i:
                if i.adult_mode and self.current_user.age < 18 :
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:     # показать видео
                    timeV=[]
                    for i.time_now in range(0,i.duration):# (секунда остановки (изначально 0)),
                        timeV.append(i.time_now+1)
                        print(i.time_now+1,end=' ')
                        sleep(1.0)
                    print(" Конец видео")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
