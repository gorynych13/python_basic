# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:
    # Конструктор
    #       B
    #       /|\
    #      / | \
    #    a/  |  \b
    #    /   |h  \
    #   /____|____\
    #  A     c    C

    def __init__(self, points_a, points_b, points_c):
        self.point_Ax = points_a[0]
        self.point_Ay = points_a[1]
        self.point_Bx = points_b[0]
        self.point_By = points_b[1]
        self.point_Cx = points_c[0]
        self.point_Cy = points_c[1]

        self.side_a = math.sqrt((self.point_Ax - self.point_Bx) ** 2 +
                                (self.point_Ay - self.point_By) ** 2)
        self.side_b = math.sqrt((self.point_Cx - self.point_Bx) ** 2 +
                                (self.point_Cy - self.point_By) ** 2)
        self.side_c = math.sqrt((self.point_Ax - self.point_Cx) ** 2 +
                                (self.point_Ay - self.point_Cy) ** 2)

    # Методы

    # Площадь
    def square(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    # Высота
    def heigh(self):
        return 2 * self.square() / self.side_c

    # Периметр
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


triangle1 = Triangle([0, 0], [2, 4], [5, 0])
triangle2 = Triangle([0, -1], [4, 4], [5, 0])
triangle3 = Triangle([-1, -2], [6, 4], [5, 0])
triangle4 = Triangle([0, 0], [0, 4], [5, 0])

print(triangle1.square())
print(triangle2.perimeter())
print(triangle3.heigh())
print(triangle4.heigh())
print(triangle4.square())
print(triangle4.perimeter())
print(triangle4.side_c)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezoid:
    # Конструктор
    #       B_____b____C
    #       /          \
    #      /            \
    #    a/              \c
    #    /                \
    #   /__________________\D
    #  A            d

    def __init__(self, points_a, points_b, points_c, points_d):
        self.point_Ax = points_a[0]
        self.point_Ay = points_a[1]
        self.point_Bx = points_b[0]
        self.point_By = points_b[1]
        self.point_Cx = points_c[0]
        self.point_Cy = points_c[1]
        self.point_Dx = points_d[0]
        self.point_Dy = points_d[1]

        # Вопрос!!! Длины сторон лучше делать как атрибуты или как методы?

        self.side_a = math.sqrt((self.point_Ax - self.point_Bx) ** 2 +
                                (self.point_Ay - self.point_By) ** 2)
        self.side_b = math.sqrt((self.point_Cx - self.point_Bx) ** 2 +
                                (self.point_Cy - self.point_By) ** 2)
        self.side_c = math.sqrt((self.point_Dx - self.point_Cx) ** 2 +
                                (self.point_Dy - self.point_Cy) ** 2)
        self.side_d = math.sqrt((self.point_Ax - self.point_Dx) ** 2 +
                                (self.point_Ay - self.point_Dy) ** 2)

    # Проверка равнобочности

    def is_equally_sides(self):
        return self.side_a == self.side_c

    # Периметр
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c + self.side_d

    def square(self):
        a = self.side_d
        b = self.side_b
        c = self.side_a
        d = self.side_c
        square = ((a + b) / 2) * math.sqrt(c ** 2 - (((a - b) ** 2 + c ** 2 - d ** 2) / (2 * (a - b))) ** 2)
        return square


print()
trapezoid1 = Trapezoid([0, 0], [1, 4], [5, 4], [6, 0])
print(trapezoid1.square())
print(trapezoid1.is_equally_sides())
print(trapezoid1.perimeter())