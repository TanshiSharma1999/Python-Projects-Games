import pgzrun
from random import randint

WIDTH = 700
HEIGHT = 550

TITLE = "Catch the Thief"

thief = Actor("thief")
thief.pos = randint(50, 650), randint(50, 500)

message = ""
score = 0
thief_alive = True
game_over = False

def reset_game():
    global score, message, thief_alive, game_over
    score = 0
    message = ""
    thief_alive = True
    game_over = False
    thief.pos = randint(50, 650), randint(50, 500)

def draw():
    screen.fill("gray")

    if thief_alive:
        thief.draw()

    screen.draw.text(f"Score = {score}", center=(100, 30), fontsize=35, color="blue")
    screen.draw.text(message, center=(500, 30), fontsize=45, color="navy")

    # Restart button (shows only when game is over)
    if game_over:
        screen.draw.text(
            "RESTART",
            center=(350, 300),
            fontsize=60,
            color="red"
        )

def on_mouse_down(pos):
    global score, message, thief_alive, game_over

    # Restart button click
    if game_over:
        if Rect((250, 260), (200, 80)).collidepoint(pos):
            reset_game()
        return

    if thief_alive and thief.collidepoint(pos):
        message = "You Caught Him!"
        score += 10
        thief.pos = randint(50, 650), randint(50, 500)

        if score == 100:
            thief_alive = False
            game_over = True
            message = "You Win! 🎉"
    else:
        thief.pos = randint(50, 650), randint(50, 500)
        score -= 10
        message = "You Missed!"

pgzrun.go()
