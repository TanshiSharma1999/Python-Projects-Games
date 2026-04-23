import pgzrun

TITLE = "Dino Run"
WIDTH = 500
HEIGHT = 500
score=0
bg = Actor("ground")
ob = Actor("cactus")
d = Actor("dino")
f=Actor("food")
d.pos = (80,335)
bg.pos = (250,250)
ob.pos = (350,365)
f.pos=(200,360)
def draw():
    screen.fill(color="white")
    bg.draw()
    d.draw()
    ob.draw()
    f.draw()
    screen.draw.text("Scrore: "+str(score),color="teal",topright=(450,10))
def update():
    global score
    """bg.x -= 2     
    if bg.right < 0:
        bg.left = WIDTH """
    ob.x-=3
    if ob.right<0:
        ob.left=WIDTH
        
    f.x-=3
    if f.right<0:
        f.left=WIDTH

    d.y+=2    
    if d.y>=335:
        d.y=335
    if d.y <240:# limits how much up it goes
        d.y=240
    if keyboard.space:
        d.y-=10 
    if d.colliderect(ob):
        score-=10
        ob.x=WIDTH
    if d.colliderect(f):
        score+=10
        f.x=WIDTH
    if f.colliderect(ob):
        f.x+=200
    
pgzrun.go()