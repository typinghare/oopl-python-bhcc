"""Canvas"""
from classes import Rectangle, Circle, Canvas

canvas = Canvas(800, 800)
rectangle0 = Rectangle(20, 20, 200, 200, stroke_color="red", fill_color="yellow")
circle0 = Circle(200, 200, 100, stroke_color="yellow", fill_color="red")
circle1 = Circle(300, 300, 50, stroke_color="yellow", fill_color="red")
canvas.add_shape(rectangle0)
canvas.add_shape(circle0)
canvas.add_shape(circle1)
canvas.draw()
