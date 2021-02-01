from firstTask import Triangle
from math import sqrt


def test_sides():
    tr1 = Triangle(-1, 0, -2)
    assert tr1.error_cases() == "Стороны должны быть больше чем 0", "Wrong error message for negative digits"
    tr2 = Triangle(2, 3, 10)
    assert tr2.error_cases() == "Такой треугольник не существует", "Wrong error message for non-existent triangle"


def test_perim():
    tr3 = Triangle(3, 4, 5)
    assert tr3.perimeter() == (tr3.a + tr3.b + tr3.c), "Perimeter is incorrect"


def test_square():
    tr4 = Triangle(3, 4, 5)
    p = tr4.perimeter()
    assert tr4.square(p) == sqrt(p/2 * (p/2 - tr4.a) * (p/2 - tr4.b) * (p/2 - tr4.c)), "Square is incorrect"


def test_types():
    tr5 = Triangle(3, 3, 3)
    assert tr5.indicate_side_type() == "Равносторонний", "Side type 'Равносторонний' is incorrect"
    tr6 = Triangle(3, 3, 2)
    assert tr6.indicate_side_type() == "Равнобедренный", "Side type 'Равнобедренный' is incorrect"
    tr7 = Triangle(3, 4, 5)
    assert tr7.indicate_side_type() == "Разносторонний", "Side type 'Разносторонний' is incorrect"
    assert tr7.indicate_edge_type() == "Прямоугольный", "Edge type 'Прямоугольный' is incorrect"


if __name__ == "__main__":
    test_perim()
    test_square()
    test_sides()
    test_types()
    print("Everything passed")
