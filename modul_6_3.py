from random import randint

class Animal: #- класс описывающий животных.
    def __init__(self, speed_: int, DANGER: int = 0):
        self.live = True
        self.sound = None            #- звук (изначально отсутствует)
        self._DEGREE_OF_DANGER = DANGER   #- степень опасности существа
        self._cords = [0, 0, 0]      #- координаты в пространстве.
        self.speed =  speed_         #- скорость передвижения существа (определяется при создании объекта)
    def move(self, dx, dy, dz):
        i = self._cords[2] + dz*self.speed
        if self._cords[2] < 0:
            print ("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx*self.speed
            self._cords[1] += dy*self.speed
            self._cords[2] = i
    def get_cords(self):#, который выводит координаты в формате:\
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")
    def attack(self):
        if self._DEGREE_OF_DANGER < 5 :
            print( "Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")
    def speak(self): #, который выводит строку со звуком sound.
        print(self.sound)

class Bird (Animal):  #- класс описывающий птиц
    def __init__(self,speed_: int,DANGER: int):
        super().__init__(speed_,DANGER)
        self.beak = True         #- наличие клюва
    def lay_eggs(self):      #, который выводит строку
        i =  randint(1, 4)      #<случайное число от 1 до 4>
        print (f"Here are(is) {i} eggs for you")

class AquaticAnimal (Animal):    # - класс описывающий плавающего животного.
    def __init__(self, speed_: int,DANGER: int = 3):
        super().__init__(speed_,DANGER)
    def dive_in(self, dz):
        self._cords[2] -= abs(dz)* int(self.speed/2)  #Этот метод должен всегда уменьшать координату z в _coords.

#Скорость движения при нырянии должна уменьшаться в 2 раза, в отличии от обычного движения.(speed / 2)

class PoisonousAnimal (Animal): #- класс описывающий ядовитых животных.
    def __init__(self, speed_: int,DANGER: int = 8):
        super().__init__(speed_, DANGER)

class Duckbill (PoisonousAnimal, Bird, AquaticAnimal):
    def __init__(self, speed_: int):
        super().__init__(speed_)
        self.sound = "Click-click-click" #- звук, который издаёт утконос


db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()