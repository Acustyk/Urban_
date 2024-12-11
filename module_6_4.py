import math

class Figure:
    def __init__(self, arg: tuple):
        self.__sides = None
        self.__color = None
        self._rejInit = True
        if arg.__len__() > 1 :      # кроме color задана хотя бы одна сторона
            self.set_color(arg[0])  #(список цветов в формате RGB)
            self.set_sides(arg[1:])
        self.filled = False  #(закрашенный, bool)
        self._rejInit = False

    def get_color(self):
        """
        :return:  возвращает список RGB цветов.
        """
        return self.__color

    def __is_valid_color(self,self2,color) :
        """
        :param принимает параметры r, g, b,
        который проверяет корректность переданных значений перед установкой нового цвета.
        Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
         """
        noCorrect = lambda x: False if isinstance(x, int) and x in range(0,255,1) else True
        if len(color) == 3 :
         for i in color:
             if noCorrect(i):
                 return False
        return True

    def set_color(self,*color):
        """
        изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. 
        Если введены некорректные данные, то цвет остаётся прежним.
        :param  принимает параметры r, g, b - числа
        """
        if len(color) == 1:
            i = color[0]
        else:
            i = color
        if self.__is_valid_color(self,i) :
            self.__color = list(i)   #(список цветов в формате RGB)

    def __is_valid_sides(self,self2,sides):
        """
        :param неограниченное кол-во сторон,
        :return: возвращает True если все стороны целые положительные числа
        и кол-во новых сторон совпадает с текущим,
        False - во всех остальных случаях.
        """
        noCorrect = lambda x: False if isinstance(x, int) and x > 0 else True
        for i in sides:
            if noCorrect(i):
                return False
        return True

    def get_sides(self):
        """
        :return:  значение атрибута __sides.
        """
        return self.__sides

    def __len__(self):
        """
        :return: периметр фигуры.
        """
        j = 0
        for i in self.__sides:
            j += i
        return  j

    def set_sides(self, *new_sides):
        """
        :param *new_sides - принимать новые стороны, если их количество не равно sides_count,
         то не изменять, в противном случае - менять.
        """
        if len(new_sides) == 1:
            if isinstance(new_sides[0], int) :
                i = list(new_sides)
            else:
                i = list(new_sides[0])
        else:
            i = new_sides
        if self.sides_count == len(i) and self.__is_valid_sides(self, i):
            self.__sides = list(i)
        elif self._rejInit :
            i = []
            for j in range(self.sides_count):
                i.append(1)
            self.__sides = i

class Circle (Figure): # круг  sides_count = 1
    def __init__(self,*arg):
       self.sides_count = 1
       super().__init__(arg)
       i = self.get_sides()
       __radius =   i[0]/(2.*3.14)     #, рассчитать исходя из длины окружности (одной единственной стороны).

    def get_square(self):
        """
        :return: возвращает площадь круга (можно рассчитать как через длину, так и через радиус
        """
        return 3.14*self.__radius**2

class Triangle (Figure): # треугольник - sides_count = 3
    def __init__(self,*arg):
        self.sides_count = 3
        super().__init__(arg)

    def get_square(self): #возвращает
        """
        :return: площадь треугольника. (можно рассчитать по формуле Герона)
        """
        sides = self.get_sides()
        p = (sides[0]+sides[1]+sides[2])/2.
        return math.sqrt(p*(p-sides[0])*(p-sides[1])*(p-sides[2]))

class Cube (Figure):    # Куб - sides_count = 12
    def __init__(self,*arg):
        self.sides_count = 12
        super().__init__(arg)
        if arg.__len__() == 2:  # кроме clolr задана одна сторона
            self._rejInit = True
            i= []
            for j in range(12): i.append(arg[1])
            self.set_sides(i)             #12 одинаковых сторон  (передаётся 1 сторона)
            self._rejInit = False

    def get_volume(self):
        """
        :return: объём куба.
        """
        sides = self.get_sides()
        return sides[0]**3


"""
#Код для проверки:
ВАЖНО!
При создании объектов делайте проверку на количество переданных сторон, 
если сторон не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, 
которое требует фигура.
Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]
"""
X1 = Circle((200, 200, 100), 10, 15, 6) # - [1]
print(X1.get_sides())
X2 = Triangle((200, 200, 100), 10, 6)   # - [1, 1, 1]
print(X2.get_sides())
X3 = Cube((200, 200, 100), 9)           # - [9, 9, 9, ....., 9] (12)
print(X3.get_sides())
X4 = Cube((200, 200, 100), 9, 12)       # - [1, 1, 1, ....., 1]
print(X4.get_sides())
X2 = Triangle((200, 200, 100), 10, 6, 12)   # - [1, 1, 1]
print(X2.get_sides(),'  square  ',X2.get_square(),'   len   ',X2.__len__())



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# Проверка объёма (куба):
print(cube1.get_volume())