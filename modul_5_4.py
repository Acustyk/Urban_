class House:
    houses_history = [] # для хранения названия созданных объектов.
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __del__(self):
        print(self.name," снесён, но он останется в истории")

    def __init__(self, name: str, level: int) -> object:
        self.name = name
        self.number_of_floors = level

    def  go_to (self, new_floor: int ):
        if 0 < new_floor <= self.number_of_floors :
            for j in range(1,new_floor+1): print(j)
        else:
            print("Такого этажа не существует ")

    def __len__(self): #- должен возвращать кол-во этажей здания self.number_of_floors.
        return self.number_of_floors
    def __str__(self): #- должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
       return "Название: " + self.name + ", кол-во этажей: " + str(self.number_of_floors)
    def __eq__(self, other): #- должен возвращать True, если количество этажей одинаковое у self и у other.
        if isinstance(other, House):
            if self.number_of_floors == other.number_of_floors :
                return True
        return False
    def __lt__(self, other):#    __lt__(<),
        if isinstance(other, House):
            if self.number_of_floors < other.number_of_floors :
                return True
        return False
    def __le__(self, other):#   __le__(<=),
        if isinstance(other, House):
            if self.number_of_floors <= other.number_of_floors :
                return True
        return False
    def __gt__(self, other):#    __gt__(>),
        if isinstance(other, House):
            if self.number_of_floors > other.number_of_floors :
                return True
        return False
    def __ge__(self, other):#    __ge__(>=),
        if isinstance(other, House):
            if self.number_of_floors >= other.number_of_floors :
                return True
        return False
    def __ne__(self, other):#    __ne__(!=)
        if isinstance(other, House):
            if self.number_of_floors != other.number_of_floors :
                return True
        return False
    def __add__(self, value)  : # - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            return NotImplemented  # Для нецелых чисел
    def __radd__(self, value)  :
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            return NotImplemented  # Для нецелых чисел

    def __iadd__(self, value: int)  :
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            return NotImplemented  # Для нецелых чисел



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3
print(House.houses_history)