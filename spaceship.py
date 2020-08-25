# Class Spaceship for Asteroids game

import math
import pyglet
from space_object import SpaceObject

ACCELERATION = 50
ROTATION_SPEED = 4  # radians per second

class Spaceship(SpaceObject):
    
    def __init__(self, window_width, window_height, batch):
        super().__init__(
            window_width // 2,
            window_height // 2,
            0,
            window_width,
            window_height,
            'images/playerShip1_blue.png',
            batch
        )
        
        # speed
        self.x_speed = 0    # pixels per second
        self.y_speed = 0    # pixels per second
                
        
    def tick(self, dt, pressed_keys):
        '''Controls move, rotation and control of spaceship'''
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
        