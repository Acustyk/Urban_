class Vehicle ():
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # , в который записан список допустимых цветов для окрашивания. (Цвета написать свои)

    def __init__(self,owner_: str, model: str, color: str, engine_power: int):
        self.owner = owner_
        self.__model = model                 #- модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power =  engine_power  #- мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__color =  color                #- название цвета. (мы не можем менять цвет автомобиля своими руками)

    def get_model (self):
        return str("Модель: " + self._Vehicle__model)

    def get_horsepower (self):
        return str("Мощность двигателя: " + str(self._Vehicle__engine_power))

    def get_color (self):
        return str("Цвет: " + self._Vehicle__color)

    def print_info (self):
        print (self.get_model())
        print (self.get_horsepower())
        print (self.get_color())
        print ("Владелец: ",self.owner)

    def set_color (self,new_color: str):
        """
        меняет цвет __color на new_color, если он есть в списке __COLOR_VARIANTS,
        в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
        """
        for i in self.__COLOR_VARIANTS:
            if i.upper() == new_color.upper():
                self.__color = new_color
                return
        print ("Нельзя сменить цвет на ",new_color)

class Sedan (Vehicle): #наследуется от класса Vehicle, а так же содержит следующие атрибуты:
    __PASSENGERS_LIMIT = 5 #(в седан может поместиться только 5 пассажиров)

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()
