#rectangle with python

import pgzrun

WIDTH=500
HEIGHT=500

colors=["red","orange","yellow","green","blue","indigo","violet"]

def draw():
    screen.fill("black")
    for i in range(1,8):
        screen.draw.filled_circle((250,250),(200-25*i),colors[i-1])#(x,y),r,c
    

pgzrun.go()