import pgzrun

WIDTH=600
HEIGHT=500

pika=Actor("pikachu")
pika.pos=(250,250)

def draw():
    screen.fill(color="white")
    pika.draw()

def update():
    if keyboard.w:
        if pika.y>70:
            pika.y-=10
    if keyboard.s:
        if pika.y<430:
            pika.y+=10
    if keyboard.a:
        if pika.x>70:
            pika.x-=10
    if keyboard.d:
        if pika.x<530:
            pika.x+=10
        

pgzrun.go()