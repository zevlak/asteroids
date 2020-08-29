# Class for effects when asteroid is destroyed

from math import pi
from random import uniform
from space_object import SpaceObject

EFFECT_LIVE = 3

class Effect(SpaceObject):
    
    def __init__(self, x, y, sprite, size, space_width, space_height):
        super().__init__(
            x,
            y,
            uniform(0, 2 * pi),
            sprite,
            space_width,
            space_height
        )
        self.sprite.opacity = 100
        self.sprite.scale = 1/size
        self.life_time = EFFECT_LIVE
    
    def tick(self, dt):
        self.life_time -= dt
        self.sprite.scale /= 1.05
        super().tick(dt)
        