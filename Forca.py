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

def drawbase():
    line.up()
    line.goto(-550,100)
    line.down()
    for a in range(2):
        line.fd(dist)
        line.rt(reto)
        line.fd(reto)
        line.rt(reto)
    

def drawhang():
    line.up()
    line.goto(-460,100)
    line.down()
    line.lt(reto)
    line.fd(dist)
    
    line.up()
    line.goto(-420,100)
    line.down()
    line.fd(dist)

    line.up()
    line.goto(-460,280)
    line.rt(reto)
    line.down()
    line.forward(dist)
    
    line.right(reto)
    line.fd(25)
    

def drawhead():
    if numero_erros==1
        line.up()
        line.goto(-300,235)
        line.down()
        line.circle(20)
    
def drawbody():
    if numero_erros==2:
        line.up()
        line.goto(-280,215)
        line.down()
        line.forward(reto)
         

def drawrarm():
    if numero_erros==3
    line.up()
    line.goto(-280,195)
    line.lt(reto/3)
    line.down()
    line.fd(reto/3+10)
    
def drawlarm():
    if numero_erros==4
    line.up()
    line.goto(-280,195)
    line.rt(dist/3)
    line.down()
    line.fd(reto/3+10)
        
def drawlleg():
    if numero_erros==5
    line.up()
    line.goto(-280,125)
    line.down()
    line.fd(dist/3)
    
def drawrleg():
    if numero_erros==6
    line.up()
    line.goto(-280,125)
    line.lt(dist/3)
    line.down()    
    line.fd(dist/3)

print("Bem-vindo ao jogo da forca")   

