'''
Turtle stamp

Donovan Wright
11/3/15
'''
import turtle
import time

s = turtle.Screen()
s.bgcolor('black')
s.title('Turtle Stamp')

time2 = {
    '3':'0',
    '2': '30',
    '1': '60',
    '12': '90',
    '11': '120',
    '10': '160',
    '9': '190',
    '8': '210',
    '7': '240',
    '6': '270',
    '5': '300',
    '4': '330'
}

t = turtle.Turtle()
t.shape('turtle')
t.shapesize(2)
t.color('white')
t.speed(0)
t.penup()
t.stamp()

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
    clock(30*x,400)

while True:
    hour = int(time.strftime("%H"))%12
    minute = time.strftime("%M")
    print('Hour:',time2[str(hour)])
    print('Minute:',minute)
