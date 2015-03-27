# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:06:50 2015

@author: Carlos
"""
import random
import turtle




archive=open("altern.txt",encoding="utf-8")
s1=archive.readlines()
keyword0= random.choice(s1)
keyword1=keyword0.lower()
keyword = keyword1.strip()
print(keyword)

accents = {"a" : "ã", "i" : "í", "o" : "ó", "o" : "ô"}


def body():
    
    if erros == 1:
        base = turtle.Turtle()          #Constroi a cabeca
        base.speed(5)
        base.penup()
        base.setpos(-225,110)
        base.pendown()
        base.pensize(10)
        base.circle(20)
        base.color("black")
    
    if erros == 2:
        base = turtle.Turtle()           #Constroi o tronco
        base.speed(5)
        base.penup()
        base.setpos(-225,110)
        base.pensize(10)
        base.pendown()
        base.left(270)
        base.forward(90)
        base.color("black")

    if erros == 3:
        base = turtle.Turtle()           #Constroi o braco esquerdo
        base.speed(5)
        base.penup()
        base.setpos(-225,90)
        base.pensize(10)
        base.pendown()
        base.left(225)
        base.forward(40)
        base.color("black")
    
    if erros == 4:
        base = turtle.Turtle()            #Constroi o braco direito
        base.speed(5)
        base.penup()
        base.setpos(-225,90)
        base.pensize(10)
        base.pendown()
        base.left(315)
        base.forward(40)
        base.color("black")

    if erros == 5:
        base = turtle.Turtle()        #Constroi a perna esquerda
        base.speed(5)
        base.penup()
        base.setpos(-225,20)
        base.pensize(10)
        base.pendown()
        base.left(240)
        base.forward(60)
        base.color("black")
    
    if erros == 6:
        base = turtle.Turtle()        #Constroi a perna direita
        base.speed(5)
        base.penup()
        base.setpos(-225,20)
        base.pensize(10)
        base.pendown()
        base.left(300)
        base.forward(60)
        base.color("black")    
        
    if erros == 7:
        base = turtle.Turtle()            #Constroi a lamina da espada
        base.speed(5)
        base.penup()
        base.setpos(-200,65)
        base.pensize(10)
        base.pendown()
        base.left(45)
        base.forward(100)
        base.color("black")
        
    
window = turtle.Screen()    # Usa a biblioteca de turtle graphics
window.bgcolor("white")     # cria uma janela
window.title("Forca")

#keyword=window.textinput("Forca", "Texto Pergunta")

base = turtle.Pen()   # Constrói a Forca
base.speed(5)
base.penup()
base.setpos(200,-200)
base.pensize(10)
base.pendown()
base.backward(500)     # anda 500 posições para tras

base.left(90)        # gira o ponteiro em 90 graus para a esquerda
base.forward(400)     # anda mais 400 posições para a frente
base.right(90)
base.forward(75)
base.right(90)
base.forward(50)
base.color("black")

'''
base.penup()
base.setpos(-250,-150)
base.write(len(keyword)*e,font=("Arial",14))
base.pensize(15)
base.hideturtle()
'''

x=len(keyword)
px = -240
py = -150

for i in range (0,x):
    if keyword[i] == " ":
        base.penup()
        base.setpos(px+i*16,py)
        base.write("  ", False, font=("Arial",14))
        
        base.hideturtle()
    else:
        base.penup()
        base.setpos(px+i*16,py)
        base.write("_ ", False, font=("Arial",14))
        
        
    
erros = 0
acertos = 0
while erros<7 and acertos<len(keyword):
    guess = window.textinput("Guess", "Write a letter.")

    if guess in keyword or accents[guess] in keyword:
            for i in range(len(keyword)):
                if guess == keyword[i] or accents[guess] == keyword[i]:
                    base.penup()
                    base.setpos(-240+i*16,-150)
                    base.pensize(15)                    
                    base.write(keyword[i],font=("Arial", 14))
                    acertos+=1
                    
                    
    else:
        erros+=1
        body()
        print(erros)
        
print(erros)
print(acertos)
window.exitonclick()
            
            
