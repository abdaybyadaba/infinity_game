import pygame
from settings import *





class Background:
    def __init__(self, sky_smoothing=0.25, ground_smoothing=1) -> None:
        self.ground = pygame.transform.scale(pygame.image.load(GR_PATH), (WIN_W, WIN_H))
        self.sky = pygame.transform.scale(pygame.image.load(BG_PATH), (WIN_W, WIN_H))
        self.offset = {"sky": 0, "ground": 0}
        self.smoothing = {"sky": sky_smoothing, "ground": ground_smoothing}

    def update(self, camera_dx) -> None:
        for key in self.offset:
            self.offset[key] = (self.offset[key] + self.smoothing[key] * camera_dx) % WIN_W

    def render(self, screen) -> None:
        screen.blit(self.sky, ((0 - self.offset["sky"]), 0))
        screen.blit(self.sky, ((WIN_W - self.offset["sky"]), 0))
        screen.blit(self.ground, (0 - self.offset["ground"], 0))
        screen.blit(self.ground, (WIN_W - self.offset["ground"], 0))


