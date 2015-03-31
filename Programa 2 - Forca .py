# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:06:50 2015

@author: Carlos
"""

import random
import turtle

base = turtle.Turtle()
scoreboardright = turtle.Turtle()
scoreboarderror = turtle.Turtle()

def limpa(lista):
    return lista

def desenhar_forca():
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

def body():
    
    if erros == 1: #Constroi a cabeca
                
        base.speed(5)
        base.penup()
        base.setheading(0)        
        base.setpos(-225,110)
        base.pendown()
        base.pensize(10)
        base.circle(20)
        base.color("black")
    
    if erros == 2: #Constroi o tronco
        base.speed(5)
        base.penup()
        base.setheading(0) 
        base.setpos(-225,110)
        base.pensize(10)
        base.pendown()
        base.left(270)
        base.forward(90)
        base.color("black")

    if erros == 3:           #Constroi o braco esquerdo
        base.speed(5)
        base.penup()
        base.setheading(0) 
        base.setpos(-225,90)
        base.pensize(10)
        base.pendown()
        base.left(225)
        base.forward(40)
        base.color("black")
    
    if erros == 4:           #Constroi o braco direito
        base.speed(5)
        base.penup()
        base.setheading(0) 
        base.setpos(-225,90)
        base.pensize(10)
        base.pendown()
        base.left(315)
        base.forward(40)
        base.color("black")

    if erros == 5:        #Constroi a perna esquerda
        base.speed(5)
        base.penup()
        base.setheading(0) 
        base.setpos(-225,20)
        base.pensize(10)
        base.pendown()
        base.left(240)
        base.forward(60)
        base.color("black")
    
    if erros == 6:        #Constroi a perna direita
        base.speed(5)
        base.penup()
        base.setheading(0) 
        base.setpos(-225,20)
        base.pensize(10)
        base.pendown()
        base.left(300)
        base.forward(60)
        base.color("black")    
        
    if erros == 7:          #Constroi a lamina da espada
        base.speed(5)
        base.penup()
        base.setheading(0) 
        base.setpos(-200,65)
        base.pensize(10)
        base.pendown()
        base.left(45)
        base.forward(100)
        base.color("black")



archive=open("entrada.txt",encoding="utf-8")
s1=archive.readlines()

# Antes de colocar a lista s1 em jogo, limpá-la

#s1 = limpa(s1)





while len(s1) > 0:

    window = turtle.Screen()    # Usa a biblioteca de turtle graphics
    window.bgcolor("white")     # cria uma janela
    window.title("Forca")
    
    keyword0= random.choice(s1)
    s1.remove(keyword0)
    

    keyword1=keyword0.lower()
    keyword = keyword1.strip()
    print(keyword)

    keywordguessed=[]   
    
    #accents = {"a" : "ã", "i" : "í", "o" : "ó", "o" : "ô"}
    
    
            
        
    
    #keyword=window.textinput("Forca", "Texto Pergunta")
    desenhar_forca()
    
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
    
    erros = 0
    acertos = 0
    
    
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
    for i in range(len(keyword)):
        if " " == keyword[i]:
            base.penup()
            base.setpos(-240+i*16,-150)
            base.pensize(15)                    
            base.write(keyword[i],font=("Arial", 14))   
            acertos+=1
    
    while erros<8 and acertos<len(keyword):
        
        guess = window.textinput("Guess", "Write a letter.")
    
        
        
        if guess in keyword:
            if guess not in keywordguessed:
                for i in range(len(keyword)):
                    if guess == " ":
                        pass   
                    elif guess == keyword[i]:
                        base.penup()
                        base.setpos(-240+i*16,-150)
                        base.pensize(15)                    
                        base.write(keyword[i],font=("Arial", 14))
                        acertos+=1
                        keywordguessed.append(guess)
                    elif guess == "a" and keyword[i]== "ã":
                        base.penup()
                        base.setpos(-240+i*16,-150)
                        base.pensize(15)                    
                        base.write(keyword[i],font=("Arial", 14))
                        acertos+=1
                        keywordguessed.append(keyword[i])
                    elif guess == "i" and keyword[i] == "í":
                        base.penup()
                        base.setpos(-240+i*16,-150)
                        base.pensize(15)                    
                        base.write(keyword[i],font=("Arial", 14))
                        acertos+=1
                        keywordguessed.append(keyword[i])
                    elif guess == "o" and keyword[i] == "ó":
                        base.penup()
                        base.setpos(-240+i*16,-150)
                        base.pensize(15)                    
                        base.write(keyword[i],font=("Arial", 14))
                        acertos+=1
                        keywordguessed.append(keyword[i])
                    elif guess == "o" and keyword[i] == "ô":
                        base.penup()
                        base.setpos(-240+i*16,-150)
                        base.pensize(15)                    
                        base.write(keyword[i],font=("Arial", 14))
                        acertos+=1
                        keywordguessed.append(keyword[i])
                    elif erros== 7:
                        base.penup()
                        base.setpos(140,150)
                        base.pensize(10)
                        base.write("Você perdeu")
                    elif acertos == len(keyword):
                        base.penup()
                        base.setpos(140,150)
                        base.pensize(10)
                        base.write("Você ganhou.")
        if erros==7 or acertos == len(keyword):
            opcao = window.textinput("Fim do jogo", "Quer jogar novamente? Sim ou Não?")
            if opcao == "Sim" or opcao == "sim"  or opcao == "SIM"  or opcao == "s":
                acertos = 9
                erros = 9
                base.reset()
                
            if opcao == "Não" or opcao == "não" or opcao == "Nao" or opcao == "nao" or opcao == "NAO" or opcao == "Não" or opcao == "n":
                erros += 1
                acertos += 1
                            
                        
        else:
            erros+=1
            body()
            print(erros)
       
        base.penup()
        base.setpos(160,180)
        base.pensize(10)
        base.write("ERROS:")
        
        scoreboarderror.reset()
        scoreboarderror.penup()
        scoreboarderror.setpos(210,180)
        scoreboarderror.write(erros)
        scoreboarderror.hideturtle()
        
        base.penup()
        base.setpos(155,190)
        base.pensize(10)
        base.write("ACERTOS:")
    
        scoreboardright.reset()
        scoreboardright.penup()
        scoreboardright.setpos(210,190)
        scoreboardright.write(acertos-keyword.count(" "))
        scoreboardright.hideturtle()
    
    
                
            
print(erros)
print(acertos)
window.exitonclick()

