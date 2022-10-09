from settings import WIN_W


class Camera:
    def __init__(self):
        self.dx = 0
        self.activated = False

    def update(self, sprite_obj):
        sprite_obj.rect.x -= self.dx

        if sprite_obj.rect.x + sprite_obj.rect.w < 0:
            sprite_obj.rect.x += WIN_W + 40

    def apply_player(self, player):
        #print(self.dx)
        x2 = player.rect.centerx
        x1 = WIN_W//2
        self.dx = x2 - x1