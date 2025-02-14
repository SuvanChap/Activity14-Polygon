#Write a program to set screen size, colour for turtle graphics and draw a polygon using turtle?

import turtle

turtle.Screen().bgcolor("green")
turtle.Screen().setup(400,400)
polygon=turtle.Turtle()
num_sides=6
side_len = 70
angle = 360.0 / num_sides

for i in range (num_sides):
    polygon.forward(side_len)
    polygon.right(angle)

turtle.done()

