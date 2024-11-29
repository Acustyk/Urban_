from tkinter.font import names


class House:
    def __init__(self, name: str, level: int):
        self.name = name
        self.number_of_floors = level

    def  go_to (self, new_floor: int ):
        if 0 < new_floor <= self.number_of_floors :
            for j in range(1,new_floor+1): print(j)
        else:
            print("Такого этажа не существует ")


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)