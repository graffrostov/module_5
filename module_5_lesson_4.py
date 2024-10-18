# Класс объектов жилого комплекса
class House:

    # __instance = None
    houses_history = []


# ------------------------------------------------------------------------------------------------------
    def __new__(cls, *args):
        # if cls.__instance is None:
        #     cls.__instance = super().__new__(cls)
        cls.houses_history.append(args[0])

        return super().__new__(cls)
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
    # Метод создания нового объекта
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(f'Создан жилой комплекс "{self.name}", '
              f'количество этажей {self.number_of_floors}')
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
    # Метод удаления объекта
    def __del__(self):
        print(f'"{self.name}" снесён, но он останется в истории')
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
    def go_to(self, new_floor):
        print(f'Жилой комплекс "{self.name}", едем на этаж {new_floor}')
        min_floor = new_floor >= 1
        max_floor = new_floor <= self.number_of_floors
        if min_floor and max_floor:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
    # Метод возвращает этажность комплекса
    def __len__(self):
        return self.number_of_floors
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
    # Метод возвращает описание жилого комплекса
    def __str__(self):
        return (f'Название: {self.name}. '
                f'Количество этажей: {self.number_of_floors}')
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# Сравнение этажности объекта с таким же объектом или с целым числом

# Сравнение на равенство
    def __eq__(self, other):

        if isinstance(other, House):
            print(f'Результат сравнения этажности {self.name} == {other.name}:')
            return self.number_of_floors == other.number_of_floors

        elif isinstance(other, int):
            print(f'Результат сравнения этажности {self.name} == {other}:')
            return self.number_of_floors == other

        else:
            print(f'Результат сравнения этажности {self.name}: '
                    f'ошибка в переданных данных')

# Сравнение меньше чем
    def __lt__(self, other):

        if isinstance(other, House):
            print(f'Результат сравнения этажности {self.name} < {other.name}:')
            return self.number_of_floors < other.number_of_floors

        elif isinstance(other, int):
            print(f'Результат сравнения этажности {self.name} < {other}:')
            return self.number_of_floors < other

        else:
            print(f'Результат сравнения этажности {self.name}: '
                  f'ошибка в переданных данных')

# Сравнение меньше или равно
    def __le__(self, other):

        if isinstance(other, House):
            print(f'Результат сравнения этажности {self.name} <= {other.name}:')
            return self.number_of_floors <= other.number_of_floors

        elif isinstance(other, int):
            print(f'Результат сравнения этажности {self.name} <= {other}:')
            return self.number_of_floors <= other

        else:
            print(f'Результат сравнения этажности {self.name}: '
                  f'ошибка в переданных данных')

# Сравнение больше чем
    def __gt__(self, other):

        if isinstance(other, House):
            print(f'Результат сравнения этажности {self.name} > {other.name}:')
            return self.number_of_floors > other.number_of_floors

        elif isinstance(other, int):
            print(f'Результат сравнения этажности {self.name} > {other}:')
            return self.number_of_floors > other

        else:
            print(f'Результат сравнения этажности {self.name}: '
                  f'ошибка в переданных данных')

# Сравнение больше или равно
    def __ge__(self, other):

        if isinstance(other, House):
            print(f'Результат сравнения этажности {self.name} >= {other.name}:')
            return self.number_of_floors >= other.number_of_floors

        elif isinstance(other, int):
            print(f'Результат сравнения этажности {self.name} >= {other}:')
            return self.number_of_floors >= other

        else:
            print(f'Результат сравнения этажности {self.name}: '
                  f'ошибка в переданных данных')

# Не равно
    def __ne__(self, other):

        if isinstance(other, House):
            print(f'Результат сравнения этажности {self.name} != {other.name}:')
            return self.number_of_floors != other.number_of_floors

        elif isinstance(other, int):
            print(f'Результат сравнения этажности {self.name} != {other}:')
            return self.number_of_floors != other

        else:
            print(f'Результат сравнения этажности {self.name}: '
                  f'ошибка в переданных данных')
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# Увеличение этажности объекта на целое число

    def __add__(self, other):

        if isinstance(other, int):
            print(f'Добавляем к {self.name} {other} этаж(а,ей)')
            self.number_of_floors += other
            return self

        else:
            print('ошибка в переданных данных, объект не изменён')
            return self

    def __radd__(self, other):
        self = self + other
        return self

    def __iadd__(self, other):
        self = self + other
        return self
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# Уменьшение этажности объекта на целое число

    def __sub__(self, other):

        if isinstance(other, int):
            print(f'Из {self.name} убраны {other} этаж(а,ей)')
            self.number_of_floors -= other
            return self

        else:
            print('ошибка в переданных данных, объект не изменён')
            return self

    def __rsub__(self, other):
        self -= other
        return self

    def __isub__(self, other):
        self -= other
        return self
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# Умножение этажности объекта на целое число
    def __mul__(self, other):

        if isinstance(other, int):
            print(f'{self.name} количество этаж(а,ей) увеличено в {other} раз(а)')
            self.number_of_floors = self.number_of_floors * other
            return self

        else:
            print('ошибка в переданных данных, объект не изменён')
            return self

    def __rmul__(self, other):
        self = self * other
        return self

    def __imul__(self, other):
        self = self * other
        return self
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# Деление
# __floordiv__ //
# __truediv__ /
# __mod__ %

# Целочисленное деление.
    def __floordiv__ (self, other):

        if isinstance(other, int):
            print(f'{self.name} количество этаж(а,ей) уменьшено в {other} раз(а)')
            self.number_of_floors = self.number_of_floors // other
            return self

        else:
            print('ошибка в переданных данных, объект не изменён')
            return self

    def __ifloordiv__(self, other):
        self = self // other
        return self

    def __rfloordiv__(self, other):
        self = self // other
        return self


# Истинное деление. Заменено на целочисленное.
    def __truediv__(self, other):

        if isinstance(other, int):
            print('Внимание! Применено целочисленное деление')
        self = self // other
        return self

    def __itruediv__(self, other):

        if isinstance(other, int):
            print('Внимание! Применено целочисленное деление')
        self = self // other
        return self

    def __rtruediv__(self, other):

        if isinstance(other, int):
            print('Внимание! Применено целочисленное деление')
        self = self // other
        return self


# Остаток от деления.
    def __mod__(self, other):

        if isinstance(other, int):
            print(f'{self.name} неделимый остаток этажей от деления на {other}')
            self.number_of_floors = self.number_of_floors % other
            return self

        else:
            print('ошибка в переданных данных, объект не изменён')
            return self

    def __imod__(self, other):
        self = self % other
        return self

    def __rmod__(self, other):
        self = self % other
        return self
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# Основное тело программы.

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

