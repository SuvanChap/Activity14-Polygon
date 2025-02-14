#Write a program to draw a square inside a square?
import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(500,500)
turtle.Screen().title("Square inside Square")
polygon = turtle.Turtle()

size = 0
while True:
    for i in range(4):
        polygon.forward(size+1)
        polygon.left(90)
        size -= 5
    size += 1

turtle.done()
