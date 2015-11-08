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

hourA = {
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
    '4': '330',
    '0': '90'
}

minuteA = {
    '00':'0',
    '01':'6',
    '02':'12',
    '03':'18',
    '04':'24',
    '05':'30',
    '06':'36',
    '07':'42',
    '08':'48',
    '09':'54',
    '10':'60',
    '11':'66',
    '12':'72',
    '13':'78',
    '14':'84',
    '15':'90',
    '16':'96',
    '17':'102',
    '18':'108',
    '19':'114',
    '20':'120',
    '21':'126',
    '22':'132',
    '23':'138',
    '24':'144',
    '25':'150',
    '26':'156',
    '27':'162',
    '28':'168',
    '29':'174',
    '30':'180',
    '31':'186',
    '32':'192',
    '33':'198',
    '34':'204',
    '35':'210',
    '36':'216',
    '37':'222',
    '38':'228',
    '39':'234',
    '40':'240',
    '41':'246',
    '42':'252',
    '43':'258',
    '44':'264',
    '45':'270',
    '46':'276',
    '47':'282',
    '48':'288',
    '49':'294',
    '50':'300',
    '51':'306',
    '52':'312',
    '53':'318',
    '54':'324',
    '55':'330',
    '56':'336',
    '57':'342',
    '58':'348',
    '59':'354'
}

color = ['blue', 'red', 'yellow', 'white', 'purple', 'green', 'magenta', 'cyan', 'orange', 'brown', 'lightblue', 'darkblue']

t = turtle.Turtle()
t.shape('turtle')
t.shapesize(2)
t.color('lightblue')
t.speed(0)
t.penup()

tsec = turtle.Turtle()
tsec.shape('turtle')
tsec.shapesize(2,stretch_len=12)
tsec.color('white')
tsec.speed(0)
tsec.penup()
tsec.stamp()

tmin = turtle.Turtle()
tmin.shape('turtle')
tmin.shapesize(2,stretch_len=8)
tmin.color('green')
tmin.speed(0)
tmin.penup()
tmin.stamp()

thour = turtle.Turtle()
thour.shape('turtle')
thour.shapesize(2, stretch_len=5)
thour.color('blue')
thour.speed(0)
thour.penup()
thour.stamp()

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

def setClock():
    hour = int(time.strftime("%H"))%12
    minute = time.strftime("%M")
    sec = time.strftime("%S")
    '''
    print('Hour:',hourA[str(hour)])
    print('Minute:',minuteA[str(minute)])
    print('Second:',minuteA[str(sec)])
    '''

    tsec.clear()
    tsec.home()
    tsec.right(int(minuteA[str(sec)])-90)
    tsec.stamp()
    
    tmin.clear()
    tmin.home()
    tmin.right(int(minuteA[str(minute)])-90)
    tmin.stamp()

    thour.clear()
    thour.home()
    thour.left(int(hourA[str(hour)])-int(minute)*0.5)
    thour.stamp()

for x in range(12):
    t.color(color[x-1])
    #print(x*30)
    clock(30*x,300)
setClock()


while True:
    setClock()
