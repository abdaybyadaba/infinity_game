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
from entities.entities import *
import os
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
        self.money = 0
        self.money_rect = pygame.transform.scale(pygame.image.load(MONEY_PATH), [40, 40])
        self.USELESS = 0

    def create_game_objects(self, player_lifes):
        self.player = Player(player_lifes)
        self.camera = Camera()
        self.next_map = self.spawner.spawn_map(0)# [object, object, object]
        self.all_sprites_group.add((self.player, self.next_map))
        self.object_sprites.add(self.next_map)


    def updates(self):
        self.USELESS += 1
        if self.camera.activated:
            self.camera.apply_player(self.player)
            self.bg.update(self.camera.dx)
            for sprite in self.all_sprites_group:
                self.camera.update(sprite)


        # if self.USELESS == 25:
           # self.money = random.randint(100_000_000_000_000_000_000, 999_999_999_999_999_999_999)
            # self.USELESS = 0



        if not self.camera.activated and self.player.rect.centerx > WIN_W:
            self.camera.activated = True

        if self.bg.offset["ground"] + self.camera.dx >= WIN_W:
            self.next_map = self.spawner.spawn_map(WIN_W)
            self.all_sprites_group.add(self.next_map)
            self.object_sprites.add(self.next_map)

        #print(len(self.all_sprites_group))
        self.all_sprites_group.update()
        self.bg.render(self.sc)
        self.all_sprites_group.draw(self.sc)
        self.update_money_bar()

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

    def check_collisions(self, collision_object):
        self.player.block_left, self.player.block_right, self.player.block_vertical = 0, 0, 0
        if isinstance(collision_object, Coin):
            collision_object.kill_object()
            self.money += 1
        if collision_object is not None:
            if self.player.rect.bottom > collision_object.rect.centery:
                if (self.player.rect.right + self.player.walk_speed) > collision_object.rect.left and \
                        self.player.rect.centerx < collision_object.rect.centerx:
                    self.player.block_right = 1
                if (self.player.rect.left - self.player.walk_speed) < collision_object.rect.right and \
                        self.player.rect.centerx > collision_object.rect.centerx:
                    self.player.block_left = 1
            if self.player.rect.bottom >= collision_object.rect.top:
                if self.player.rect.bottom < collision_object.rect.centery:
                    self.player.rect.bottom = collision_object.rect.top+5
                self.player.block_vertical = 1

    def update_money_bar(self):
        self.sc.blit(self.money_rect, [1 + 30, 445])
        for i, u in enumerate(str(self.money)):
            self.sc.blit(pygame.transform.scale(pygame.image.load(os.path.join(COUNTS_PATH, "{}.png".format(u))), [40, 40]),
                         [int(i)*30 + 75, 445])


    def do_player_action(self):
        l = pygame.sprite.spritecollideany(self.player, self.object_sprites)
        # if l is None and self.player.rect.y <= 400:
        #     self.player.direction_idx = 2
        # print(l)
        self.check_collisions(l)
        if not self.player.is_jump:
            self.player.move_player(0, 0, self.object_sprites, self.player)
        else:
            self.player.jump(self.object_sprites, self.player)

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







