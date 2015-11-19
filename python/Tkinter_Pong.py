'''
Pong
Donovan Wright
10/13/15
'''

from tkinter import *
import random
import time
import os
import subprocess

class Ball:
 def __init__(self, canvas, paddle, color):
  self.canvas = canvas
  self.paddle1 = paddle1
  self.paddle2 = paddle2
  self.id = canvas.create_oval(10, 25, 60, 60, fill=color)
  self.canvas.move(self.id, 245, 100)
  starts = [-3, -2, -1, 1, 2, 3]
  random.shuffle(starts)
  self.x = starts[0]
  self.y = -3
  self.canvas_height = self.canvas.winfo_height()
  self.canvas_width = self.canvas.winfo_width()
  self.hit_bottom = False

 def hit_paddle(self, pos):
  paddle_pos = self.canvas.coords(self.paddle1.id)
  if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
   if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
    return True
  return False

 def hit_paddle2(self, pos):
  paddle_pos = self.canvas.coords(self.paddle2.id)
  if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
   print('1')
   if pos[3] >= paddle_pos[1] and pos[3] >= paddle_pos[3]:
    return True
  return False
 
 
 def draw(self):
  self.canvas.move(self.id, self.x, self.y)
  pos = self.canvas.coords(self.id)
  if pos[1] <= 0:
   self.y = 3
   #print('Top hit')
  if pos[3] >= self.canvas_height:
   self.hit_bottom = True
   global score
   time.sleep(1)
   self.x= -10
   self.y = -10
   self.hit_bottom = False
   score = 0
   speak("You-lose...")
   print('Score:',score)
  if self.hit_paddle(pos) == True:
   self.y = -3
   global score
   score += 1
   speakS = 'Score-'+str(score)
   speak(str(score))
   print(speakS)

   if self.hit_paddle2(pos) == True:
    self.y = 3
    global score
    score += 1
    speakS = 'Score-'+str(score)
    speak(str(score))
    print(speakS)
  if pos[0] <= 0:
   self.x = 3
  if pos[2] >= self.canvas_width:
   self.x = -3
  
class Paddle1:
 def __init__(self, canvas, color):
  self.canvas = canvas
  self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
  self.canvas.move(self.id, 200, 700)
  self.x = 0
  self.canvas_width = self.canvas.winfo_width()
  self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
  self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
  
 def draw(self):
  self.canvas.move(self.id, self.x, 0)
  pos = self.canvas.coords(self.id)
  if pos[0] <= 0:
   self.x = 0
  elif pos[2] >= self.canvas_width:
   self.x = 0
 def turn_left(self, evt):
  self.x = -4
 def turn_right(self, evt):
  self.x = 4

class Paddle2:
 def __init__(self, canvas, color):
  self.canvas = canvas
  self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
  self.canvas.move(self.id, 200, 100)
  self.x = 0
  self.canvas_width = self.canvas.winfo_width()
  self.canvas.bind_all('<KeyPress-KP_4>', self.turn_left)
  self.canvas.bind_all('<KeyPress-KP_6>', self.turn_right)
  
 def draw(self):
  self.canvas.move(self.id, self.x, 0)
  pos = self.canvas.coords(self.id)
  if pos[0] <= 0:
   self.x = 0
  elif pos[2] >= self.canvas_width:
   self.x = 0
 def turn_left(self, evt):
  self.x = -4
 def turn_right(self, evt):
  self.x = 4




wait = 0
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=800, height=800, bd=0, highlightthickness=0, bg='black')
canvas.pack()
tk.update()
paddle1 = Paddle1(canvas, 'blue')
paddle2 = Paddle2(canvas, 'red')
ball = Ball(canvas, paddle1, 'lightblue')
score = 0
os.system("/home/compsci/Donovan/cena.mp3")

def speak(word):
    bashCommand = "espeak -a 150 "+word+" &"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
while 1:
 if ball.hit_bottom == False:
  ball.draw()
  paddle1.draw()
  paddle2.draw()
  wait += .0000000000000001
 tk.update_idletasks()
 tk.update()
 time.sleep(0.01-wait)

