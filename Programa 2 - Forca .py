# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:06:50 2015

@author: Carlos
"""

import turtle


def head():
    base = turtle.Turtle()          #Constroi a cabeca
    base.speed(5)
    base.penup()
    base.setpos(-225,110)
    base.pendown()
    base.circle(20)
    base.color("black")
    
def body():
    base = turtle.Turtle()           #Constroi o tronco
    base.speed(5)
    base.penup()
    base.setpos(-225,110)
    base.pendown()
    base.left(270)
    base.forward(90)
    base.color("black")

def left_arm():
    base = turtle.Turtle()           #Constroi o braco esquerdo
    base.speed(5)
    base.penup()
    base.setpos(-225,90)
    base.pendown()
    base.left(225)
    base.forward(40)
    base.color("black")
    
def right_arm():
    base = turtle.Turtle()            #Constroi o braco direito
    base.speed(5)
    base.penup()
    base.setpos(-225,90)
    base.pendown()
    base.left(315)
    base.forward(40)
    base.color("black")

def left_leg():
    base = turtle.Turtle()        #Constroi a perna esquerda
    base.speed(5)
    base.penup()
    base.setpos(-225,20)
    base.pendown()
    base.left(240)
    base.forward(60)
    base.color("black")
    
def right_leg():
    base = turtle.Turtle()        #Constroi a perna direita
    base.speed(5)
    base.penup()
    base.setpos(-225,20)
    base.pendown()
    base.left(300)
    base.forward(60)
    base.color("black")    
    
def sword():
    base = turtle.Turtle()            #Constroi a lamina da espada
    base.speed(5)
    base.penup()
    base.setpos(-200,65)
    base.pendown()
    base.left(45)
    base.forward(100)
    base.color("black")
    
window = turtle.Screen()    # Usa a biblioteca de turtle graphics
window.bgcolor("white")     # cria uma janela
window.title("Forca")

keyword=window.textinput("Forca", "Texto Pergunta")

base = turtle.Pen()   # Constrói a Forca
base.speed(5)
base.penup()
base.setpos(200,-200)
base.pendown()
base.backward(500)     # anda 500 posições para tras
base.left(90)        # gira o ponteiro em 90 graus para a esquerda
base.forward(400)     # anda mais 400 posições para a frente
base.right(90)
base.forward(75)
base.right(90)
base.forward(50)
base.color("black")

guess1 = window.textinput("First guess", "Digite uma letra.")

if guess1 not in keyword:
    head()
else:
    pass

guess2 = window.textinput("Second guess", "Digite uma letra.")

if guess2 not in keyword:
    body()
else:
    pass

guess3 = window.textinput("Second guess", "Digite uma letra.")
if guess3 not in keyword:
    left_arm()
else:
    pass

guess4 = window.textinput("Second guess", "Digite uma letra.")
if guess4 not in keyword:
    right_arm()
else:
    pass

guess5 = window.textinput("Second guess", "Digite uma letra.")
if guess5 not in keyword:
    left_leg()
else:
    pass

guess6 = window.textinput("Second guess", "Digite uma letra.")
if guess6 not in keyword:
    right_leg()
else:
    pass

guess7 = window.textinput("Second guess", "Digite uma letra.")
if guess7 not in keyword:
    sword()
else:
    pass

