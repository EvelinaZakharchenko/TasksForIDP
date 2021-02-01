# Написать класс треугольник.
# В конструкторе определить длины сторон.
# Добавить методы для вычисления площади, периметра,
# определения типа треугольника (прямой, равнобедренный, равносторонний, разносторонний)
# Написать тесты для покрытия данного кода
from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self, perimeter):
        p = perimeter / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def indicate_side_type(self):
        if self.a == self.b == self.c:
            return "Равносторонний"
        elif self.a == self.b or self.a == self.c or self.c == self.b:
            return "Равнобедренный"
        else:
            return "Разносторонний"

    def indicate_edge_type(self):
        if self.a**2 == (self.b**2 + self.c**2) or self.b**2 == (self.a**2 + self.c**2) or self.c**2 == (self.b**2 + self.a**2):
            return "Прямоугольный"
        else:
            return "НЕ прямоугольный"

    def error_cases(self):
        if self.a <= 0 or self.a <= 0 or self.a <= 0:
            return "Стороны должны быть больше чем 0"
        elif self.a >= self.b + self.c or self.b >= self.a + self.c or self.c >= self.b + self.a:
            return "Такой треугольник не существует"


if __name__ == "__main__":
    first = int(input("Ввведите первую сторону: "))
    second = int(input("Ввведите вторую сторону: "))
    third = int(input("Ввведите третью сторону: "))
    Triangle1 = Triangle(first, second, third)
    Triangle1.error_cases()
    perim = Triangle1.perimeter()
    print("Периметр:", perim)
    print("Площадь:", Triangle1.square(perim))
    print(Triangle1.indicate_side_type())
    print(Triangle1.indicate_edge_type())
