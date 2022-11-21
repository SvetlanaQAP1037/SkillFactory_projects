import math

# 16.8.1-16.8.2

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b
class Scuare:
    def __init__(self, a):
        self.a = a
    def get_area_scuare(self):
        return  self.a ** 2
class Circle:
    def __init__(self, r):
        self.r = r
    def get_area_circle(self):
        return self.r * math.pi ** 2