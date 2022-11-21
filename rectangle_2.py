from task_16_8_2 import Rectangle, Scuare, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Scuare(5)
square_2 = Scuare(10)

print(square_1.get_area_scuare(), square_2.get_area_scuare())

figures = [rect_1, rect_2, square_1, square_2]
for figure in figures:
    if isinstance(figure, Scuare):
        print(figure.get_area_scuare())
    else:
        print(figure.get_area())

circle_1 = Circle(5)
circle_2 = Circle(8)

print("%.2f" % (circle_1.get_area_circle()), "%.2f" % (circle_2.get_area_circle()))

