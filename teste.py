# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:52:04 2015

@author: Vitor
"""

import turtle
window= turtle.Screen()
window.bgcolor("lightblue")
window.title("Hangman")
turtle.screensize(600,860)

line= turtle.Turtle()
t1= turtle.Turtle()
t2= turtle.Turtle()
line.speed(4)
line.pensize(8)


reto= 90
dist=180
dist1=100   

import Forca.py
print("Bem-vindo ao jogo da forca")
drawbase()
drawhang()

import random

biblioteca= open("entrada.txt","r").readline()
numero_erros=0
numero_chutes=0
numero_vitorias=0
chutes=[]

while numero_erros<6:
    palavra= random.choice(biblioteca)
    letra= window.textinput("Digite uma letra", "Letra:")
    chutes.append(letra)
    t2.up()
    t2.setpos(-450,50)
    for b in len(palavra):
        t2.down()
        t2.fd(dist2/4)
        t2.up()
        t2.fd(5)
        
        
    if len(letra)!=1
        print("Digite apenas uma letra")
        return letra
        
    elif letra in palavra and not in chutes
        t1.write(letra,font=("Arial",50,"normal"))
        print("Você acertou!")
        numero_chutes+=1
        
    elif letra not in palavra and not in chutes:
        numero_chutes+=1
        numero_erros+=1
        drawhead()
        drawbody()
        drawrarm()
        drawlarm()
        drawrleg()
        drawlleg()
       
      else print("Você já escolheu esse caractere")
          return letra
         
      elif palavra in chutes
      print("Você venceu! Está a salvo.")
      


turtle.done()