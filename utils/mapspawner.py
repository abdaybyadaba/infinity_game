import random
from entities.entities import *


class ObjectsFactory:
    def __init__(self):
        self.objects_fabric = {"bigbox": Box,
                                 "3verticalboxes": ThreeVerticalBoxes,
                                 "middlebox": MiddleBox,
                                 "smallbox": SmallBox,
                                 "boxwithapples": BoxWithApples,
                                 "barrel": Barrel,
                                 "cartoonbox": CartoonBox,
                                 "coin": Coin
                                }

    def get_object(self, string_object):
        return self.objects_fabric[string_object]#(напиши сюда координаты)


class MapSpawner:
    def __init__(self, maps):
        self.maps = maps
        self.objects_factory = ObjectsFactory()

    def spawn_map(self, bias=0) -> list:
        objects = []
        for i in random.sample(self.maps, 1):
            for item in i:
                x = (item["coords"][0]*WIN_W)//WIN_W_MAP + bias
                y = item['coords'][1]
                objects.append(self.objects_factory.get_object(item['object_type'])(x, y))# Mob(x,y)
        return objects




