from turtle import *

speed('fastest')

rt(270)

seth(90)

angle = 20

def tree(level, size):
    if level > 0:
        stamp()

        width(level * 0.5)

        fd(size)

        lt(angle)
        tree(level - 1, size * 0.8)

        rt(angle*2)
        tree(level - 1, size * 0.8)

        lt(angle)

        bk(size)     

        shapesize(2) 
   

def draw(level):

    colormode(255)

    pu()

    home()

    hideturtle()
    seth(90)

    bk(200)

    pd()

    pencolor('brown')
    shape("circle")
    resizemode("user")
    fillcolor('green')

    tree(level, 120)

draw(5)

input()