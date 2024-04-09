"""
библиотеку для поставки внешним клиентам, 
которая умеет вычислять площадь круга по радиусу  S = π * r²
и треугольника по трем сторонам. 


- Легкость добавления других фигур

"""
from math import pi
import inspect

class Figure():
    def get_area(self):
        raise NotImplementedError('Must implement get_area()')


# Класс квадрата
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2

# Класс треугольника
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        # проверка может ли такой треугольник существовать
        if self.a + self.b < self.c and self.a + self.c < self.b and self.b + self.c < self.a:
            raise ValueError("The sides do not form a triangle")

    def get_area(self):
        #? проверка является ли треугольник прямоугольным, для прямоугольных треугольников своя формула
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return self.a * self.b / 2
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


#! Чтобы добавить фигуру в библотеку, нужно добавить ее в список figures
def getArea(*args, **kwargs): 
    figures = [Circle, Triangle]
    names = []
    length = []
    for i in figures:
        names.append(i.__name__)
        length.append(len(inspect.signature(i.__init__).parameters)-1)
    
    params = dict(zip(names, length))
    if len(args) in params.values():
        for i in figures:
            if len(args) == params[i.__name__]:
                return i(*args).get_area()
    else:
        raise ValueError("Incorrect number of arguments")
        
        
