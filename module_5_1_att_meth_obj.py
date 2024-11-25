class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(f'В здании {self.name} {self.number_of_floors} этажей:')
        self.go_to(30)                                                 # вызов метода go_to внутри метода __init__ для
                                                                       # всех объектов данного класса House:h1, h2, h3

    def go_to (self, new_floor):
        self.new_floor = new_floor

        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'Вы набрали {self.new_floor}-й этаж: такого этажа не существует')
        else:
            for i in range(0, new_floor):
                i += 1
                print(i)




h1 = House('"ЖК Эльбрус"', 30)
h2 = House('"Домик в деревне"', 5)
h3 = House('"ЖК Горский"', 18)

h3.go_to(-3)                                                         # вызов метода go_to для объекта h3 класса House