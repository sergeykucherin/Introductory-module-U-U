import random
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print (f'{self.sound}')

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        number_eggs = [1, 2, 3, 4]
        _lay_egg = random.choice(number_eggs)
        print(f"Here are(is) {_lay_egg} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        new_z = self._cords[2] - dz * (self.speed / 2)
        self._cords[2] = int(new_z)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()

# Лекция. Множественное наследование. Метод super.

# class Human:
#     def __init__(self, name, group):
#         self.name = name
#         super().__init__(group)
#         super().about()
#
#     def info(self):
#         print(f'Hello, my name is {self.name}')
#
# class StudentGroup:
#     def __init__(self, group):
#         self.group = group
#
#     def about(self):
#         print(f'{self.name} is teaching in {self.group} ')
#
# class Student(Human, StudentGroup):
#     def __init__(self, name, place, group):
#         # Human.__init__(self, name)
#         super().__init__(name, group)
#         self.place = place
#         super().info()
#
#
# # human = Human('John')
# # print(human.name)
# student = Student('Maksim', 'Urban', 'Python 17')
#
# print(Student.mro())
# print(Human.mro())
# print(StudentGroup.mro())