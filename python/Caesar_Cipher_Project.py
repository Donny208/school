import time

letters = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'z':24,
    'y':25,
    'z':26,
    ' ':27,
    '-':28,
    '0':29,
    '1':30,
    '2':31,
    '3':32,
    '4':33,
    '5':34,
    '6':35,
    '7':36,
    '8':37,
    '9':38,
    '.':39,
    '!':40,
    ',':41,
    '?':42,
    '/':43,
    ':':44
}
numbers = {
    '*1*':'a',
    '*2*':'b',
    '*3*':'c',
    '*4*':'d',
    '*5*':'e',
    '*6*':'f',
    '*7*':'g',
    '*8*':'h',
    '*9*':'i',
    '*10*':'j',
    '*11*':'k',
    '*12*':'l',
    '*13*':'m',
    '*14*':'n',
    '*15*':'o',
    '*16*':'p',
    '*17*':'q',
    '*18*':'r',
    '*19*':'s',
    '*20*':'t',
    '*21*':'u',
    '*22*':'v',
    '*23*':'w',
    '*24*':'x',
    '*25*':'y',
    '*26*':'z',
    '*27*':' ',
    '*28*':'-',
    '*29*':'0',
    '*30*':'1',
    '*31*':'2',
    '*32*':'3',
    '*33*':'4',
    '*34*':'5',
    '*35*':'6',
    '*36*':'7',
    '*37*':'8',
    '*38*':'9',
    '*39*':'.',
    '*40*':'!',
    '*41*':',',
    '*42*':'?',
    '*43*':'/',
    '*44*':':'
}

gMessage = ''
gNumber = ''
gKey = int(0)
gLength = int(0)
count = 0
finalMessage = ''

def start():
    global gMessage, gKey
    s = input('-----\nWould you like to (E)encode, (D)decode, (c)Crack or (Q)quit> ')
    time.sleep(0.25)
    if s.lower() == 'e':
        key = int(input('What do you want your key to be> '))
        time.sleep(0.25)
        gKey = key
        encodeMes = input('What message do you want to encode> ').lower()
        time.sleep(0.25)
        gMessage = encodeMes
        encode(encodeMes,key)
    elif s.lower() == 'c':
        crackMes = input('What Message do you want to crack')
        time.sleep(0.25)
        gKey = 0
        for x in range(0,len(numbers)-2):
            crack(crackMes,x)
            print(gKey)
            gKey += 1

    if s.lower() == 'd':
        key = int(input('What do you want your key to be> '))
        time.sleep(0.25)
        gKey = key*-1
        decodeMes = input('What message do you want to decode> ').lower()
        time.sleep(0.25)
        gMessage = decodeMes
        encode(decodeMes,key)
        
    elif s.lower() == 'q':
        quit()

def encode(message,key):
    global gKey, gLength
    print('Plain Text:',message)
    gLength = len(message)
    for x in range(0,len(message)):
        if letters[message[x]]+gKey <= len(numbers):
            num(x,len(message),letters[message[x]]+gKey)
        elif letters[message[x]]+gKey > len(numbers):
            num(x,len(message),letters[message[x]]+gKey-len(numbers))

def crack(message,key):
    global gKey, gLength
    print('Plain Text:',message)
    gLength = len(message)
    for x in range(0,len(message)):
        if letters[message[x]]+gKey >= 1:
            num(x,len(message),letters[message[x]]+gKey)
        elif letters[message[x]]+gKey <= 0:
            num(x,len(message),letters[message[x]]+gKey+len(numbers))
        elif letters[message[x]]+gKey <= len(numbers):
            num(x,len(message),letters[message[x]]+gKey)
        elif letters[message[x]]+gKey > len(numbers):
            num(x,len(message),letters[message[x]]+gKey-len(numbers))

def num(x,xEnd,number):
        global gMessage, gNumber, count, finalMessage, gLength, gKey
        numberTwo = '*'+str(number)+'*'
        gNumber = gNumber + str(numberTwo)
        if x == xEnd-1:
            print('Encoded Message Step 1:',gNumber)
            time.sleep(0.25)
            for x in range(0,gLength):
                attack = gNumber[gNumber.index('*'):gNumber.index('*',2)+1]
                finalMessage = finalMessage + numbers[attack]
                gNumber = gNumber.replace(attack,'',1)
                if x == gLength-1:
                    print('Encoded Message Step 2:',finalMessage)
                    print('-----\n')
                    time.sleep(0.25)
            finalMessage = ''
            #gNumber = ''
            #gMessage = ''
            #gKey = 0
            #gLength = 0
            start()
start()
