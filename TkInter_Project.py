from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=800, height=800)
canvas.pack()

def create_col(num):
    colNum = 800/num
    colNumO = 800/num
    for x in range(num-1):
        canvas.create_line(colNum,0,colNum,800)
        colNum += colNumO

def create_row(num):
    rowNum = 800/num
    rowNumO = 800/num
    for x in range(num-1):
        canvas.create_line(0,rowNum,800,rowNum)
        rowNum += rowNumO

col = int(input('How Many Columns?> '))
row = int(input('How Many Rows?> '))

create_col(col)
create_row(row)

    
    
