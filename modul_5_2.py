class House:
    def __init__(self, name: str, level: int):
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


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))