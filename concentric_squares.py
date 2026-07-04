#rectangle with python

import pgzrun

WIDTH=400
HEIGHT=400

colors=["red","orange","yellow","green","blue","indigo","violet"]

def draw():
    screen.fill("red")
    for i in range(1,8):
        screen.draw.filled_rect(Rect((i*25,i*25),(350-(i*50),350-(i*50))),colors[i-1])#(x,y),(w,h),c
   

pgzrun.go()