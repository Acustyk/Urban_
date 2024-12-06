class Plant:
    def __init__(self, name: str, edible: bool = False):
        self.name = name        #  - индивидуальное название каждого растения
        self.edible = edible     #(съедобность)

class Animal:
    def __init__(self,name: str):
        self.name  = name     # - индивидуальное название каждого животного.
        self.alive = True     #(живой)
        self.fed   = False    #(накормленный),
    def eat(self, food: Plant):
        if food.edible :
            print("<",self.name,"> съел <",food.name,">")
            self.fed = True
        else:
            print("<",self.name,"> не стал есть <",food.name,">")
            self.alive = False

class Mammal (Animal):
    pass

class Predator (Animal):
    pass

class Flower(Plant):
    pass

class Fruit (Plant):
    def __init__(self, name: str, edible: bool = True):
        super().__init__(name,edible)



a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
