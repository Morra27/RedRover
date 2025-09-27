# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
# rect = Rectangle(2, 4)
# a = rect.area()
# b = rect.perimeter()
# print(a)
# print(b)


class Car:
    def __init__(self, make, max_speed, speed = 0):
        self.make = make
        self.max_speed = max_speed
        self.speed = speed
    def display_speed(self):
        print(self.speed)
    def accelerate(self):
        if self.speed + 10 < self.max_speed:
            self.speed += 10
        else:
            self.speed = self.max_speed
    def brake(self):
        if self.speed - 10 > 0:
            self.speed -= 10
        else:
            self.speed = 0

my_toyota = Car("Toyota", 180, 65)
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.display_speed()
