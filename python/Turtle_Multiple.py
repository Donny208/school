import turtle
import time

s = turtle.Screen()
s.bgcolor('black')
s.title('Turtle Stamp')

t = turtle.Turtle()
t.shape('turtle')
t.shapesize(2)
t.color('lightblue')
t.speed(0)
t.penup()

t2 = turtle.Turtle()
t2.shape('turtle')
t2.shapesize(2)
t2.color('lightgreen')
t2.speed(0)
t2.width(5)
'''
t.penup()
t.forward(100)
t.pendown()
t.forward(25)
t.penup()
t.forward(25)
t.stamp()

t.back(150)
t.left(90)
t.forward(100)
t.pendown()
t.forward(25)
t.penup()
t.forward(25)
t.stamp()

t2.left(180)
t2.penup()
t2.forward(100)
t2.pendown()
t2.forward(25)
t2.penup()
t2.forward(25)
t2.stamp()

t2.home()
t2.left(270)
t2.penup()
t2.forward(100)
t2.pendown()
t2.forward(25)
t2.penup()
t2.forward(25)
t2.stamp()
'''

color = ['blue', 'red', 'yellow', 'white', 'purple', 'green', 'magenta', 'cyan', 'orange', 'brown', 'lightblue', 'darkblue']
def clock(d,x):
    t.home()
    t.left(d)
    t.forward(x-100)
    t.pendown()
    t.forward(30)
    t.penup()
    t.forward(50)
    t.left(180)
    t.stamp()

for x in range(12):
    t.color(color[x-1])
    #print(x*30)
    clock(30*x,300)


t2.home()
t2.forward(275)
t2.right(100)
t2.penup()
t2.forward(75)
t2.right(10)
t2.stamp()
time.sleep(0.1)
t2.clear()
t2.forward(60)

while True:
    t2.right(16)
    t2.forward(76)
    time.sleep(0.1)
