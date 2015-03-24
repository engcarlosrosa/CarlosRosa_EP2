# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:06:50 2015

@author: Carlos
"""

import turtle

window = turtle.Screen()    # Usa a biblioteca de turtle graphics
window.bgcolor("white")     # cria uma janela
window.title("Forca")

variavel_texto = window.textinput("Forca", "Texto Pergunta") 

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

guess1 = window.textinput("Forca", "Texto Pergunta")

if variavel_texto != guess1:
    base = turtle.Turtle()          #Constroi a cabeca
    base.speed(5)
    base.penup()
    base.setpos(-225,110)
    base.pendown()
    base.circle(20)
    base.color("black")
else:
    pass


base = turtle.Turtle()           #Constroi o tronco
base.speed(5)
base.penup()
base.setpos(-225,110)
base.pendown()
base.left(270)
base.forward(90)
base.color("black")


base = turtle.Turtle()           #Constroi o braco esquerdo
base.speed(5)
base.penup()
base.setpos(-225,90)
base.pendown()
base.left(225)
base.forward(40)
base.color("black")


base = turtle.Turtle()            #Constroi o braco direito
base.speed(5)
base.penup()
base.setpos(-225,90)
base.pendown()
base.left(315)
base.forward(40)
base.color("black")


base = turtle.Turtle()        #Constroi a perna esquerda
base.speed(5)
base.penup()
base.setpos(-225,20)
base.pendown()
base.left(240)
base.forward(60)
base.color("black")


base = turtle.Turtle()        #Constroi a perna direita
base.speed(5)
base.penup()
base.setpos(-225,20)
base.pendown()
base.left(300)
base.forward(60)
base.color("black")

base = turtle.Turtle()            #Constroi a base da espada
base.speed(5)
base.penup()
base.setpos(-200,80)
base.pendown()
base.left(315)
base.forward(30)
base.color("black")

base = turtle.Turtle()            #Constroi a lamina da espada
base.speed(5)
base.penup()
base.setpos(-200,65)
base.pendown()
base.left(45)
base.forward(100)
base.color("black")


window.exitonclick()