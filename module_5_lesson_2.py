class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(f'Жилой комплекс "{self.name}", количество этажей {self.number_of_floors}')

    def go_to(self, new_floor):
        print(f'Жилой комплекс "{self.name}", едем на этаж {new_floor}')
        if new_floor >= 1 and new_floor < self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return (self.number_of_floors)


    def __str__(self):
        return (f'Название: {self.name}. Количество этажей: {self.number_of_floors}')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

print(h1)
print(h2)

print(len(h1))
print(len(h2))