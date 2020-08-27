# Class Spaceship for Asteroids game

import math
import pyglet
from space_object import SpaceObject

ACCELERATION = 50
ROTATION_SPEED = 4  # radians per second

class Spaceship(SpaceObject):
    
    def __init__(self, x, y, sprite, space_width, space_height):
        super().__init__(
            x,
            y,
            0,
            sprite,
            space_width,
            space_height
        )
                        
        
    def tick(self, dt, pressed_keys):
        '''Move spaceship'''
        # rotation
        if pyglet.window.key.LEFT in pressed_keys:
            self.rotation += dt * ROTATION_SPEED
        if pyglet.window.key.RIGHT in pressed_keys:
            self.rotation -= dt * ROTATION_SPEED
       
        # move
        if pyglet.window.key.UP in pressed_keys:
            self.x_speed += dt * ACCELERATION * math.cos(self.rotation)
            self.y_speed += dt * ACCELERATION * math.sin(self.rotation)
        
        super().tick(dt)
        