import sys
import pygame
from app import App

pygame.init()
max_player_lifes = 5
score = 0
app = App(max_player_lifes)


while True:
    app.run()
    if app.player.n_lifes:
        continue_game = True
        score = app.progress
        lifes = app.player.n_lifes

    else:
        print("added new score", app.progress)
        continue_game = app.game_over()
        score = 0
        lifes = max_player_lifes




