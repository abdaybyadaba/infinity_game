import sys
import pygame.sprite
from pygame_menu import widgets
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
from pygame_widgets.progressbar import ProgressBar


# git commit -a -m "fixed" в Terminal

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
        self.heart_rect = pygame.transform.scale(pygame.image.load(HEART_PATH), [40, 40])
        self.gold_heart_rect = pygame.transform.scale(pygame.image.load(GOLD_HEART_PATH), [40, 40])
        self.lasttime_conflict = 0

    def create_game_objects(self, player_lifes):
        self.player = Player(player_lifes)
        self.camera = Camera()
        self.next_map = self.spawner.spawn_map(0), self.spawner.spawn_map(WIN_W)  # [object, object, object]
        self.all_sprites_group.add((self.player, *self.next_map))
        self.object_sprites.add(*self.next_map)

    def updates(self):

        if self.camera.activated:
            if self.player.direction_idx == -1:
                self.camera.activated = False
            else:
                self.camera.apply_player(self.player)
                self.bg.update(self.camera.dx)
                for sprite in self.all_sprites_group:
                    self.camera.update(sprite)

        if not self.camera.activated and self.player.rect.centerx > WIN_W // 2:
            self.camera.activated = True


        if self.bg.offset["ground"] + self.camera.dx >= WIN_W:
            print(self.bg.offset["ground"])
            self.next_map = self.spawner.spawn_map(WIN_W)
            self.all_sprites_group.add(self.next_map)
            self.object_sprites.add(self.next_map)

        # print(len(self.all_sprites_group))
        self.all_sprites_group.update()
        self.bg.render(self.sc)
        self.all_sprites_group.draw(self.sc)
        self.update_health_bar()
        self.update_lives_bar()

        pygame.display.update()

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def show_death_message(self):
        font = pygame.font.SysFont("Arial", 30)
        text_render = font.render("press space to restart game, your score: {} ".format(self.progress), True,
                                  TEXT_COLOR)
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

    def check_collisions(self, collision_objects):
        self.player.block_left, self.player.block_right, self.player.block_vertical = 0, 0, 0

        for obj in collision_objects:
            if isinstance(obj, Coin):
                obj.kill_object()
                self.player.health = self.player.health + MEDKIT_XP_STEP if \
                    self.player.health + MEDKIT_XP_STEP < MAX_XP else MAX_XP

            if isinstance(obj, Turtle) and (time.time() - self.lasttime_conflict > 4):
                self.lasttime_conflict = time.time()
                self.player.health = self.player.health - 50 if self.player.health >= 50 else 0
                obj.death = True
                #collision_object.death_action()

            if isinstance(obj, AirdropBox):
                obj.kill_object()
                if self.player.health < MAX_XP:
                    self.player.health = self.player.health + ADRENALINE_XP_STEP if \
                        self.player.health + ADRENALINE_XP_STEP < MAX_XP else MAX_XP
                elif self.player.addition_health < MAX_ADDITIONAL_XP:
                    self.player.addition_health = self.player.addition_health + ADRENALINE_XP_STEP if \
                        self.player.addition_health + ADRENALINE_XP_STEP < MAX_XP else MAX_XP

            if isinstance(obj, MobBox):
                if self.player.rect.bottom > obj.rect.centery:
                    if (self.player.rect.right + self.player.walk_speed) > obj.rect.left and \
                            self.player.rect.centerx < obj.rect.centerx:
                        self.player.block_right = 1
                    if (self.player.rect.left - self.player.walk_speed) < obj.rect.right and \
                            self.player.rect.centerx > obj.rect.centerx:
                        self.player.block_left = 1
                if self.player.rect.bottom >= obj.rect.top:
                    if self.player.rect.bottom < obj.rect.centery:
                        self.player.rect.bottom = obj.rect.top + 5
                    self.player.block_vertical = 1

    def update_health_bar(self):
        # self.progress_bar = widgets.ProgressBar("kookok", pos=(30, 445))
        # print(type(self.sc))
        # self.progress_bar.draw(pygame.Surface(self.sc))
        self.progress_bar = ProgressBar(self.sc, 30, 445, 170, 30, lambda: self.player.health / MAX_XP,
                                        completedColour="#eb3700", )
        self.progress_bar.draw()
        # self.sc.blit(self.heart_rect, [1 + 30, 445])
        # for i, u in enumerate(str(self.player.health)):
        #     self.sc.blit(pygame.transform.scale(pygame.image.load(os.path.join(COUNTS_PATH, "{}.png".format(u))), [40, 40]),
        #                  [int(i)*30 + 75, 445])

    def update_lives_bar(self):
        self.progress_bar = ProgressBar(self.sc, 30 + 170, 445, 85, 30,
                                        lambda: self.player.addition_health / MAX_ADDITIONAL_XP,
                                        completedColour="#cfaf1a", )
        self.progress_bar.draw()
        # self.sc.blit(self.gold_heart_rect, [1 + 230, 445])
        # for i, u in enumerate(str(self.player.addition_health)):
        #     self.sc.blit(pygame.transform.scale(pygame.image.load(os.path.join(COUNTS_PATH, "{}.png".format(u))), [40, 40]),
        #                  [int(i)*30 + 275, 445])

    def do_player_action(self):
        #l = pygame.sprite.spritecollideany(self.player, self.object_sprites)
        l = pygame.sprite.spritecollide(self.player, self.object_sprites, False, collided=pygame.sprite.collide_mask)
        # if l is None and self.player.rect.y <= 400:
        #     self.player.direction_idx = 2
        # print(l)
        print(l)
        self.check_collisions(l)
        if not self.player.is_jump:
            self.player.move_player()
        else:
            self.player.jump()

    def run(self):

        while True:
            self.check_event()
            self.clock.tick(FPS)
            # self.bg.
            self.do_player_action()

            # if  == 0:
            #     return True
            # print(0)
            self.updates()
