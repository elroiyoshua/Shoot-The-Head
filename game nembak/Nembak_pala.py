import pgzrun
from random import randint

kepala = Actor("kepaladedod2")

def draw():
    screen.clear()
    kepala.draw()

def place_kepala():
    kepala.x = randint(10, 800)
    kepala.y = randint(10, 600)


def on_mouse_down(pos):
    if kepala.collidepoint(pos):
        print("Good shoot!")
        place_kepala()
    else:
        print("you missed")
        quit()

place_kepala()
pgzrun.go()
