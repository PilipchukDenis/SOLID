
# O — Open-Closed (Принцип открытости-закрытости)
# class Vehicle:
#     def __init__(self, max_speed):
#         self.max_speed = max_speed
#
#     def get_max_speed(self):
#         return self.max_speed
#
#
#     def calculate_allowed_speed(self):
#         raise NotImplementedError("Этот метод должен быть реализован в подклассах")
#
#
#
# class Car(Vehicle):
#     def calculate_allowed_speed(self):
#         return self.get_max_speed() * 0.8
#
#
#
# class Bus(Vehicle):
#     def calculate_allowed_speed(self):
#         return self.get_max_speed() * 0.6
#
#
# class SpeedCalculation:
#     def calculate_allowed_speed(self, vehicle: Vehicle) -> float:
#         return vehicle.calculate_allowed_speed()
#
#
#
# if __name__ == "__main__":
#     car = Car(max_speed=200)
#     bus = Bus(max_speed=100)
#
#     speed_calculator = SpeedCalculation()
#
#     print(f"Разрешенная скорость для автомобиля: {speed_calculator.calculate_allowed_speed(car)} км/ч")
#     print(f"Разрешенная скорость для автобуса: {speed_calculator.calculate_allowed_speed(bus)} км/ч")
#######################################################################################################


#  S – Single Responsibility (Принцип единственной ответственности)

# class Employee:
#     def __init__(self, name, dob, base_salary):
#         self.name = name
#         self.dob = dob
#         self.base_salary = base_salary
#
#     def get_emp_info(self):
#         return f"name - {self.name}, Denis - {self.dob}"
#
#     def get_base_salary(self):
#         return self.base_salary
#
#
#
# class SalaryCalculator:
#     def __init__(self, tax_rate: float = 0.25):
#         self.tax_rate = tax_rate
#
#     def calculate_net_salary(self, employee: Employee) -> float:
#         base_salary = employee.get_base_salary()
#         tax = base_salary * self.tax_rate
#         return base_salary - tax
#
#
#
# if __name__ == "__main__":
#     employee = Employee(name="Pilipchuk Denis", dob="1923-26-09", base_salary=5000)
#     salary_calculator = SalaryCalculator()
#
#
#     print(employee.get_emp_info())
#
#
#     net_salary = salary_calculator.calculate_net_salary(employee)
#     print(f"Чистая заработная плата: {net_salary}")
#

#######################################################################################################
#  I — Interface Segregation (Принцип разделения интерфейсов)


# from abc import ABC, abstractmethod
# import math
#
# class Shape2D(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Shape3D(ABC):
#     @abstractmethod
#     def volume(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape2D):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius * self.radius
#
#
# class Cube(Shape3D):
#     def __init__(self, edge):
#         self.edge = edge
#
#     def area(self):
#         return 6 * self.edge * self.edge
#
#     def volume(self):
#         return self.edge * self.edge * self.edge
#
#
# if __name__ == "__main__":
#     circle = Circle(radius=5)
#     cube = Cube(edge=3)
#
#     print(f"Площадь круга: {circle.area()}")
#     print(f"Площадь куба: {cube.area()}")
#     print(f"Объем куба: {cube.volume()}")

#######################################################################################################

# L — Liskov Substitution (Принцип подстановки Барбары Лисков)
#
# from abc import ABC, abstractmethod
#
# class Quadrilateral(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Rectangle(Quadrilateral):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def set_width(self, width):
#         self.width = width
#
#     def set_height(self, height):
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# class Square(Quadrilateral):
#     def __init__(self, side_length):
#         self.side_length = side_length
#
#     def set_side_length(self, side_length):
#         self.side_length = side_length
#
#     def area(self):
#         return self.side_length * self.side_length
#
#
# if __name__ == "__main__":
#     rectangle = Rectangle(10, 5)
#     print(f"Площадь прямоугольника: {rectangle.area()}")
#
#     square = Square(5)
#     print(f"Площадь квадрата: {square.area()}")
#
#     square.set_side_length(7)
#     print(f"Площадь квадрата после изменения длины стороны: {square.area()}")
#
