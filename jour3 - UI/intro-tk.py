#!/usr/bin/env python
# coding: utf-8

# In[9]:


from tkinter import Tk, Label, Button
from tkinter import TOP, BOTTOM, LEFT, RIGHT

fen = Tk()

label = Label(fen, text="Bonjour tout le monde!")
label.pack(side=BOTTOM)

button1 = Button(fen, text="Boutton 1")
# button1.pack(side=LEFT, expand=True, fill='both')
button1.pack(side=LEFT, expand=True, fill='y')

button2 = Button(fen, text="Boutton 2")
button2.pack()

button3 = Button(fen, text="Boutton 3")
button3.pack()

fen.mainloop()


# In[11]:



from tkinter import Tk, Label, Button
from tkinter import TOP, BOTTOM, LEFT, RIGHT

fen = Tk()

button1 = Button(fen, text="Boutton 1")
button1.grid(row=2,column=0)

button2 = Button(fen, text="Boutton 2")
button2.grid(row=1,column=0)

button3 = Button(fen, text="Boutton 3")
button3.grid(row=1,column=1)

fen.mainloop()


# In[12]:


from tkinter import Tk, Label, Button
from tkinter import TOP, BOTTOM, LEFT, RIGHT
from itertools import product

fen = Tk()

for i, j in product(range(3),range(3)):
    button1 = Button(fen, text=f"Boutton {i}-{j}")
    button1.grid(row=i,column=j)

fen.mainloop()


# In[17]:


from tkinter import Tk, Label, Button, Frame
from tkinter import TOP, BOTTOM, LEFT, RIGHT
from itertools import product

fen = Tk()

label = Label(fen, text="Hello")
label.pack()

frame = Frame(fen)
frame.pack()

for i, j in product(range(3),range(3)):
    button1 = Button(frame, text=f"{i}-{j}", width=6, height=3)
    button1.grid(row=i,column=j)

fen.mainloop()


# In[41]:


from tkinter import Tk, Label, Button, Frame, StringVar
from tkinter import TOP, BOTTOM, LEFT, RIGHT
from itertools import product
import re

fen = Tk()

def print_valider():
    print("Valider")
    displayed_value = chaine.get()
    result = eval(displayed_value[1:] if displayed_value[0] == "0" else displayed_value)
    chaine.set(result)

def print_operator(e):
    print("operator", e.widget.value_op)
    value = chaine.get()
    value += e.widget.value_op
    chaine.set(value)

def print_operator_click_right(e):
    print("right", e.widget.value_op)

class ButtonOp(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self.value_op = kwargs['text']

chaine = StringVar()
chaine.set("0")
label = Label(fen, textvariable=chaine, height=3)
label.pack()

btn_valider = Button(fen, text="valider", height=3, command=print_valider)
btn_valider.pack(side=BOTTOM, expand=True, fill='x')

frame_op = Frame(fen)
frame_op.pack(side=RIGHT)

btn_zero = Button(fen, text="0", height=3)
btn_zero.pack(side=BOTTOM, expand=True, fill='x')

frame_num = Frame(fen)
frame_num.pack()

for op in ['+','-','*','/']:
    button = ButtonOp(frame_op, text=op, width=6, height=3)
    button.pack()
    button.bind('<Button-1>', print_operator)
    button.bind('<Button-3>', print_operator_click_right)

for i, j in product(range(3),range(3)):
    button1 = ButtonOp(frame_num, text=str(3*(2-i) + j + 1), width=6, height=3)
    button1.grid(row=i,column=j)
    button1.bind('<Button-1>', print_operator)

fen.mainloop()


# In[42]:


# -*- coding: utf-8 -*-
from tkinter import *
from itertools import product


class OpButton(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self.operator = kwargs['text']
    

class NumberButton(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self.value = kwargs['text']
    
    def print_number(self):
        print('number', self.value)


class Calculatrice:
    def __init__(self):
        self.fen = Tk()
        
        self.operand_1 = 0
        self.operand_2 = 0
        self.operator= '+'
        
        self.value = StringVar()
        self.value.set("")
        self.label = Label(self.fen, textvariable=self.value, height=2)
        self.label.pack(side=TOP, expand=True, fill='both')    
    
        self.button_valider = Button(self.fen, text="Valider", height=2) #, command=valider)
        self.button_valider.bind('<Button-1>', self.handle_validate)
        self.button_valider.pack(
                side=BOTTOM,
                expand=True,
                fill='both')
        
        self.frame_op = Frame(self.fen)
        self.frame_op.pack(side=RIGHT)
        
        self.button_zero = NumberButton(self.fen, text="0", height=2)
        self.button_zero.pack(
                side=BOTTOM,
                expand=True,
                fill='both')
        self.button_zero.bind('<Button-1>', self.handle_number)
        
        self.frame_number = Frame(self.fen)
        self.frame_number.pack()
        
        for op in ['+','-','*','/']:
            btn = OpButton(self.frame_op, text=op, width=5, height=2)
            btn.pack()
            btn.bind('<Button-1>', self.handle_op)
        #    btn.bind('<Button-1>', print_op)
        
        for i,j in product(range(3), range(3)):
            button = NumberButton(self.frame_number, text="%d"%(3*(2-i)+j+1), width=5, height=2)
            button.grid(row=i, column=j)
            button.bind('<Button-1>', self.handle_number)
        
        self.fen.mainloop()
    
    def handle_number(self, e):
        curr_operand = self.value.get() + e.widget.value
        self.value.set(curr_operand)
        self.operand_2 = int(curr_operand)
    
    def handle_op(self, e):
        if self.operator == '+':
            self.operand_1 += self.operand_2
        if self.operator == '-':
            self.operand_1 -= self.operand_2
        if self.operator == '*':
            self.operand_1 *= self.operand_2
        if self.operator == '/':
            self.operand_1 /= self.operand_2
        self.operand_2 = 0
        self.value.set('')
        self.operator = e.widget.operator
        
    def handle_validate(self, e):
        if self.operator == '+':
            self.operand_1 += self.operand_2
        if self.operator == '-':
            self.operand_1 -= self.operand_2
        if self.operator == '*':
            self.operand_1 *= self.operand_2
        if self.operator == '/':
            self.operand_1 /= self.operand_2
        self.operand_2 = 0
        self.value.set(str(self.operand_1))
    
calc = Calculatrice()


# In[52]:


from tkinter import Tk, PhotoImage, Canvas
from time import sleep

fen =Tk()

canvas = Canvas(fen, width=600, height=600)
canvas.pack()

image = PhotoImage(file="pomp.png")

i = 0
def display():
    global i
    i+=1
    canvas.delete("all")
    canvas.create_image(i*20 % 500,i*20 % 500,image=image)
    canvas.after(200, display)

display()
fen.mainloop()


# In[2]:


class Voiture:
    """
     attribut:
         - couleur = par défaut à 'rouge'
         - vitesse_max = 180
         - position 
    """
    def __init__(self, position_initiale, couleur='rouge'):
        self.position = np.array(position_initiale)
        self.couleur = couleur
        self.vitesse_max = 180
        self.direction = np.array([1,0])

    def avancer(self):
        nouvelle_position = self.position + self.direction
        if (nouvelle_position > 0).all() and (nouvelle_position < 10).all():
#        if nouvelle_position[0] < 10 and nouvelle_position[0] >= 0 \
#            and nouvelle_position[1] < 10 and nouvelle_position[1] >= 0:
            self.position = nouvelle_position
        else:
            self.tourner()
            self.avancer()
        
    def tourner(self):
        self.direction = np.array([[0,-1],[1,0]]).dot(self.direction)
        
from tkinter import Tk, PhotoImage, Canvas
# from time import sleep
import numpy as np

fen =Tk()

canvas = Canvas(fen, width=640, height=640)
canvas.pack()

image = PhotoImage(file="pomp.png")
voiture = Voiture([2,3])

def display():
    voiture.avancer()
    canvas.delete("all")
    canvas.create_image(
        voiture.position[0]*64 ,
        voiture.position[1]*64,
        image=image
    )
    canvas.after(200, display)

display()
fen.mainloop()


# In[ ]:




