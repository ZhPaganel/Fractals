from turtle import *

speed('fastest')

rt(270)

seth(90)

angle = 30
pu()
setpos(0, -200)
pd()

def tree(level, size):
    if level > 0:

        colormode(255)
    
        pencolor(0, 255//level, 0)

        fd(size)

        lt(angle)
        tree(level - 1, size * 0.8)

        pencolor(0, 255//level, 0)

        rt(angle*2)
        tree(level - 1, size * 0.8)

        pencolor(0, 255//level, 0)

        lt(angle)
        bk(size)     

tree(14, 120)

input()
