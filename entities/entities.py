import pygame.sprite
import pygame
from settings import *
from utils.spritesheet import SpriteSheet
import time

class Mob(pygame.sprite.Sprite):
    def __init__(self, coords, path_to_sprite, scale_width, scale_height):
        super().__init__()
        self.anim_number = 0
        self.scale = (scale_width, scale_height)
        self.coords = coords
        self.frame_cords = self.coords[self.anim_number]
        self.sprite_sheet = SpriteSheet(path_to_sprite)
        self.image = pygame.transform.scale(self.sprite_sheet.get_image(*self.frame_cords), self.scale)

    def update(self):
        self.frame_cords = self.coords[self.anim_number // len(self.coords)]
        self.image = pygame.transform.scale(self.sprite_sheet.get_image(*self.frame_cords), self.scale)
        self.anim_number = 0 if (self.anim_number + 1) == len(self.coords)*5 else self.anim_number + 1
        self.destroy_object()

    def kill_object(self):
        pygame.sprite.Sprite.kill(self)

    def destroy_object(self):
        if self.rect.bottomright[0] <= 7:
            self.kill_object()


class Coin(Mob):
    def __init__(self, x, y):
        super().__init__(COIN_CAS, COIN_SPRITESHEET_PATH, 30, 30)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)


class MobBox(Mob):
    def __init__(self, coords, path_to_sprite, scale_width, scale_height, x, y):
        super().__init__(coords, path_to_sprite, scale_width, scale_height)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)

    def update(self):
        self.destroy_object()

class Box(MobBox):
    def __init__(self, x, y):
        super().__init__(Big_box, DIFFERENT_BOXES_SPRITESHEET_PATH, 187//1.5, 127//1.5, x, y)

class ThreeVerticalBoxes(MobBox):
    def __init__(self, x, y):
        super().__init__(Vertical_boxes, DIFFERENT_BOXES_SPRITESHEET_PATH, 84//1.5, 154//1.5, x, y)


class MiddleBox(MobBox):
    def __init__(self, x, y):
        super().__init__(medium_box, DIFFERENT_BOXES_SPRITESHEET_PATH, 138//1.5, 97//1.5, x, y)



class SmallBox(MobBox):
    def __init__(self, x, y):
        super().__init__(smalle_box, DIFFERENT_BOXES_SPRITESHEET_PATH, 87//1.5, 54//1.5, x, y)



class BoxWithApples(MobBox):
    def __init__(self, x, y):
        super().__init__(box_with_apples1, DIFFERENT_BOXES_SPRITESHEET_PATH, 90//1.5, 76//1.5, x, y)



class Barrel(MobBox):
    def __init__(self, x, y):
        super().__init__(barrel1, DIFFERENT_BOXES_SPRITESHEET_PATH, 109//1.5, 113//1.5, x, y)



class CartoonBox(MobBox):
    def __init__(self, x, y):
        super().__init__(cartoon_box1, DIFFERENT_BOXES_SPRITESHEET_PATH, 125//1.5, 84//1.5, x, y)



class BoxWithCat(MobBox):
    def __init__(self, x, y):
        super().__init__(box_with_cat1, DIFFERENT_BOXES_SPRITESHEET_PATH, 118//1.5, 93//1.5, x, y)


