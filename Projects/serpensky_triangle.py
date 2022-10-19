from turtle import *
speed (100)
right(30)
shape('triangle')
pu()

hideturtle()

def sierpinski(size,order):
    if order == 0:
        stamp()
    else :
        for i in range (0,3):
            forward (size)
            sierpinski(size/2,order-1)

            backward(size)

            left(120)

sierpinski(180,4)

exitonclick()