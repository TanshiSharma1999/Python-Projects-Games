import pgzrun
import random

WIDTH=700
HEIGHT=500
TITLE="Walk on the Beach"

#create characters needed
bg=Actor("sunset")
bg.pos=(350,250)

banana=Actor("banana")
banana.pos=(350,50)

poison=Actor("poison")
poison.pos=(250,50)

ava=Actor("avacado2")
ava.pos=(200,400)

score=0 # to track the score
#to draw the images and text
def draw():
    bg.draw()
    ava.draw()
    banana.draw()
    poison.draw()
    screen.draw.text("Score: "+str(score),(610,10),fontsize=30)

def update():
    global score
    #key movements
    if keyboard.left:
        ava.x=ava.x-10
        if ava.x<50:#bound the character on the screen
            ava.x=50
    elif keyboard.right:
        ava.x=ava.x+10
        if ava.x>650:#bound the character on the screen
            ava.x=650
    #moves banana down in loop
    banana.y+=5
    if banana.y>500:
        banana.y=0
        banana.x=random.randint(50,450)
    poison.y+=5
    #move posison down in a loop
    if poison.y>500:
        poison.y=0
        poison.x=random.randint(50,450)
    #add score    
    if ava.distance_to(banana) < 50:
        score += 1
        banana.y = 0
        banana.x = random.randint(50, 650)
    #lose score
    if ava.distance_to(poison) < 50:
        score -= 1
        poison.y = 0
        poison.x =random.randint(50,650)
pgzrun.go()
