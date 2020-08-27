# Class Asteroid for Asteroids game

from math import pi
from random import randrange, uniform
from space_object import SpaceObject

MAX_SPEED = 100
MAX_ROTATION = 5


class Asteroid(SpaceObject):
    
    def __init__(self, x, y, sprite, space_width, space_height):
        super().__init__(
            x,
            y,
            uniform(0,2 * pi),
            sprite,
            space_width,
            space_height
        )
        
        self.x_speed = randrange(-MAX_SPEED, MAX_SPEED)
        self.y_speed = randrange(-MAX_SPEED, MAX_SPEED)
        self.rotation_speed = uniform(-MAX_ROTATION, MAX_ROTATION)

    
    def tick(self, dt):
        '''Moves asteroid'''
        self.rotation += dt * self.rotation_speed
        super().tick(dt)