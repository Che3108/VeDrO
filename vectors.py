#!/usr/bin/python3

from math import pi, cos, sin

class Vector_2D(object):
    '''
    Вектор в двумерном пространстве.
        start_point - начальная точка вектора
        size - длина вектора
        angle - угол между вектором и осью OX (0..360) 
    '''
    def __init__(self,
                 start_point:tuple[int, int],
                 size:int,
                 angle:int) -> None:
        self.__start_point = start_point
        self.__scale, self.__size = self.__calc_size(1.0, size)
        self.__angle_grad, self.__angle_rad =  self.__grad2rad(angle)

    def __grad2rad(self, angle_grad:int) -> tuple[int, float]:
        '''Перевод градусов в радианы.'''
        angle_grad = angle_grad % 360
        angle_rad  = (angle_grad * pi) / 180
        return (angle_grad, angle_rad)

    def __calc_size(self, scale:float, size:int) -> tuple[float, int]:
        '''Масштабирование длины вектора.'''
        size= int(round(size * abs(scale), 0))
        return (scale, size)

    def __calc_end_point(self, 
                         start_point:tuple[int, int],
                         size:int,
                         angle_rad:float) -> tuple[int, int]:
        '''Вычисление конечной точки вектора.'''
        x_start, y_start = start_point
        x_calc = size * cos(angle_rad)
        y_calc = size * sin(angle_rad)
        x_end = int(round(x_calc + x_start, 0))
        y_end = int(round(y_calc + y_start, 0))
        return (x_end, y_end)

    def __calc_all_poilts(self,
                          start_point:tuple[int, int],
                          end_point:tuple[int, int]) -> tuple[tuple[int, int], ...]:
        '''Вычисление всех точек вектора.'''
        sort_revers = True
        x_1, y_1 = start_point
        x_2, y_2 = end_point
        x_min = min([x_1, x_2])
        x_max = max([x_1, x_2])
        y_min = min([y_1, y_2])
        y_max = max([y_1, y_2])
        points = []
        if x_1 == x_2:
            for y in range(y_min, y_max + 1):
                points.append((x_1, y))
        else:
            a = (y_2 - y_1) / (x_2 - x_1)
            b = y_1 - a * x_1
            for x in range(x_min, x_max + 1):
                y = a * x + b
                points.append((x, int(round(y, 0))))
        points = list(set(points))
        if x_min == x_1:
            sort_revers = False
        points.sort(key=lambda x: x[0], reverse=sort_revers)
        return tuple(points)

    def get_points(self) -> tuple[tuple[int, int], ...]:
        '''Получить координаты всех точек вектора.
           Координаты точек расположены по порядку от начальной до конечной.'''
        end_point = self.__calc_end_point(self.__start_point,
                                          self.__size,
                                          self.__angle_rad)
        points = self.__calc_all_poilts(self.__start_point, end_point)
        return points

    @property
    def angle(self):
        '''Угол между вектором и осью OX (0..360).'''
        return self.__angle_grad

    @angle.setter
    def angle(self, angle:int) -> None:
        self.__angle_grad, self.__angle_rad =  self.__grad2rad(angle)

    @property
    def end_point(self) -> tuple[int, int]:
        '''Координаты конечной точки вектора (только чтение).'''
        end_point = self.__calc_end_point(self.__start_point,
                                          self.__size,
                                          self.__angle_rad)
        return end_point

    @property
    def size(self) -> int:
        '''Длина вектора (только чтение).'''
        return self.__size

    @property
    def scale(self) -> float:
        '''Коэффициент масштабирования вектора.'''
        return self.__scale

    @scale.setter
    def scale(self, scale:float) -> None:
        self.__scale, self.__size = self.__calc_size(scale, self.__size)

    @property
    def start_point(self) -> tuple[int, int]:
        '''Координаты начальной точки вектора.'''
        return self.__start_point
    
    @start_point.setter
    def start_point(self, start_point:tuple[int, int]) -> None:
        self.__start_point = start_point



if __name__ == "__main__":
    # Создаем объект
    v = Vector_2D((2,2), 3, 30)
    print('Начальная точка:', v.start_point)
    print('Длина:', v.size)
    print('Угол:', v.angle)
    print('Масштаб:', v.scale)
    print('Точки вектора:\n\t', v.get_points())
    # Меняем масштаб
    v.scale = 2.0
    print('Точки вектора после масштабирования:\n\t', v.get_points())
