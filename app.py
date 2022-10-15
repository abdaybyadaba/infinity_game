import sys
import pygame.sprite
import random
from pygame.locals import *
from sprites.player import Player
from settings import *
from utils.camera import Camera
from entities.entities import *
from sprites.background import Background
from maps import maps
import random
from utils.mapspawner import MapSpawner

#git commit -a -m "fixed" в Terminal

class App:
    def __init__(self, player_lifes, progress=0):
        self.bg = Background()
        self.spawner = MapSpawner(maps)
        self.sc = pygame.display.set_mode((WIN_W, WIN_H))
        self.clock = pygame.time.Clock()
        self.all_sprites_group = pygame.sprite.Group()
        self.object_sprites = pygame.sprite.Group()
        self.progress = progress
        self.create_game_objects(player_lifes)


    def create_game_objects(self, player_lifes):
        self.player = Player(player_lifes)
        self.camera = Camera()
        self.next_map = self.spawner.spawn_map(0)# [object, object, object]
        self.all_sprites_group.add((self.player, self.next_map))
        self.object_sprites.add(self.next_map)


    def updates(self):
        if self.camera.activated:
            self.camera.apply_player(self.player)
            self.bg.update(self.camera.dx)
            for sprite in self.all_sprites_group:
                self.camera.update(sprite)


        if not self.camera.activated and self.player.rect.centerx > WIN_W:
            self.camera.activated = True

        if self.bg.offset["ground"] + self.camera.dx >= WIN_W:
            self.next_map = self.spawner.spawn_map(WIN_W)
            self.all_sprites_group.add(self.next_map)
            self.object_sprites.add(self.next_map)

        print(len(self.all_sprites_group))
        self.all_sprites_group.update()
        self.bg.render(self.sc)
        self.all_sprites_group.draw(self.sc)

        pygame.display.update()


    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def show_death_message(self):
        font = pygame.font.SysFont("Arial", 30)
        text_render = font.render("press space to restart game, your score: {} ".format(self.progress), True, TEXT_COLOR)
        self.sc.fill((0, 0, 0))
        X, Y = (WIN_W - text_render.get_size()[0]) / 2, (WIN_H - text_render.get_size()[1]) / 2
        self.sc.blit(text_render, (X, Y))

    def game_over(self):
        self.show_death_message()

        pygame.display.flip()
        pygame.event.clear()
        while True:
            event = pygame.event.wait()
            if event.type == QUIT:
                return False
            elif event.type == KEYDOWN and event.key == pygame.K_SPACE:
                return True

    def do_player_action(self):

        if not self.player.is_jump:
            if not pygame.sprite.spritecollideany(self.player, self.object_sprites):
                can_go = True
                self.player.move_player(0, 0, )

        else:
            self.player.jump()

    def run(self):

        while True:
            self.check_event()
            self.clock.tick(FPS)
            #self.bg.
            self.do_player_action()

            # if  == 0:
            #     return True
            # print(0)
            self.updates()







