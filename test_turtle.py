# création carré
import turtle

def square(length):
    for side in range(4):
        turtle.forward(length)
        turtle.left(90)

turtle.reset()
square(200)
turtle.exitonclick()