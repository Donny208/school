#import turtle
import random
#pen = turtle.Pen()
#turtle.bgcolor('black')
#sides = 3

colors = ['red', 'blue', 'green', 'pink','white']
'''
for x in range(5000):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides+1)
    t.width(10)
    t.speed(0)
'''
def square():
    for x in range(0,4):
        pen.pencolor(colors[random.randint(0,4)])
        pen.forward(300)
        pen.left(90)
    circle()
    
def triangle():
    pen.left(180)
    pen.forward(130)
    pen.left(270) # going up
    pen.color('black')
    pen.forward(70)
    pen.left(270)
    for x in range(3):
        pen.width(5)
        pen.pencolor(colors[random.randint(0,4)])
        pen.forward(260)
        pen.left(120)
    
def circle():
    pen.forward(150)
    pen.pencolor(colors[random.randint(0,4)])
    pen.circle(150)
    triangle()
square()

def start():
    shape = int(input('How Many Sides Do You Want?> '))
    length = int(input('Line Distance?> '))
    shapeDraw()


    
    
