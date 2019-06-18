# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
import functools
import operator

# родительский класс для геометрических фигур
class GeometricFigure:
    def __init__(self, *apex):
        # принимаем список с координатами вершин и храним его в словаре {номер вршины: [x, y]}
        self.coor = {key + 1: apex[key] for key in range(len(apex))}

    # метод для рассчета длин сторон фигуры (не зависит от количества сторон в фигуре)
    def side(self):
        self.sides = {}
        for key in self.coor:
            if key != len(self.coor):
                self.sides[key] = round(math.sqrt((self.coor[key][0] - self.coor[key + 1][0]) ** 2 +
                                                  (self.coor[key][1] - self.coor[key + 1][1]) ** 2), 2)
            else:
                self.sides[key] = round(math.sqrt((self.coor[key][0] - self.coor[1][0]) ** 2 +
                                                  (self.coor[key][1] - self.coor[1][1]) ** 2), 2)
        return self.sides

    # метод для рассчета периметра (суммируем все стороны фигуры из метода side()
    def perimeter(self):
        self.p = sum([self.side()[key] for key in self.coor])
        return self.p

    # метод для рассчета полупериметра, необходим для вычисления площадей фигур
    def half_perimetr(self):
        self.p2 = self.perimeter() / 2
        return self.p2

# класс для работы с треугольниками
class Triangle(GeometricFigure):
    def __init__(self, *apex):
        super().__init__(*apex)

    # метод рассчета площади треугольника (берется одна высота из метода heigth() и сторона трегольника на которую
    # эта высота опирается
    def square(self):
        s = round(((self.height()[1] * self.side()[1]) / 2), 2)
        return s

    # метод для рассчета всех высот трегольника
    def height(self):
        self.heights = {}
        for key in self.side():
            self.heights[key] = round((2 * math.sqrt(self.half_perimetr() * (self.half_perimetr() - self.side()[1]) *
                                                     (self.half_perimetr() - self.side()[2]) *
                                                     (self.half_perimetr() - self.side()[3])) / self.side()[key]), 2)
        return self.heights


t1 = Triangle([2, 1], [6, 2], [3, 7])
print('Длины сторон треугольника:')
for i in t1.side():
    print(f'- сторона {i}: {t1.side()[i]}')
print(f'Периметр треугольника: {t1.perimeter()}')
print(f'Площадь треугольника: {t1.square()}')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# класс равнобедренной трапеции
class IsoscelesTrapezoid(GeometricFigure):
    def __init__(self, *apex):
        super().__init__(*apex)

    # метод рассчета площади равнобедренной трапеции по формуле Брахмагупты sqrt((p/2-a)*(p/2-b)*(p/2-c)*(p/2-d))
    def square(self):
        # с помощью генератора собираем список множителей, с помощью reduce и mul перемножаем все элементы списка
        s = round(math.sqrt(functools.reduce(operator.mul, [self.half_perimetr() -
                                                            self.side()[key] for key in self.side()])), 2)
        return s

    # метод проверки является ли трапеция равнобедренной, если диагонали трапеции равны, то она — равнобедренная
    def is_isosceles(self):
        if math.sqrt((self.coor[1][0] - self.coor[3][0]) ** 2 + (self.coor[1][1] - self.coor[3][1]) ** 2) == \
                     math.sqrt((self.coor[2][0] - self.coor[4][0]) ** 2 + (self.coor[2][1] - self.coor[4][1]) ** 2):
            return 'Трапеция равнобедренная'
        else:
            return 'Трапеция не равнобедренная'


trap1 = IsoscelesTrapezoid([40, 120], [120, 40], [240, 40], [320, 120])
print()
print(trap1.is_isosceles())
print('Длины сторон трапеции:')
for i in trap1.side():
    print(f'- сторона {i}: {trap1.side()[i]}')
print(f'Периметр трапеции: {trap1.perimeter()}')
print(f'Площадь трапеции: {trap1.square()}')
