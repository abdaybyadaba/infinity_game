import random
from entities.entities import *


class ObjectsFactory:
    def __init__(self):
        self.objects_fabric = {"bigbox": Box,
                                 "3verticalboxes": ThreeVerticalBoxes,
                                 "middlebox": MiddleBox,
                                 "smallbox": SmallBox,
                                 "boxwithapples": BoxWithApples,
                                 "barrel": AirdropBox,
                                 "cartoonbox": CartoonBox,
                                 "coin": Coin,
                                 "turtle": Turtle,
                                 "cannon": Cannon
                                }

    def get_object(self, string_object):
        return self.objects_fabric[string_object] #(на пиши сюда координаты)


class MapSpawner:
    def __init__(self, maps):
        self.maps = maps
        self.objects_factory = ObjectsFactory()

    def spawn_map(self, bias=0) -> dict:
        print(f"New map with {bias=}")
        objects = {}
        for i in random.sample(self.maps, 1):
            for item in i:
                x = (item["coords"][0]*WIN_W)//WIN_W_MAP + bias
                y = item['coords'][1]
                type = item['object_type']
                if type == 'turtle' and random.randint(1, 10) <= 4:
                    continue

                objects[type] = self.objects_factory.get_object(type)(x, y, item['xdev'], item['v'])
                                                 # Mob(x,y)
        return objects




