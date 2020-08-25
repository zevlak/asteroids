# Class Spaceship for Asteroids game

import math
import pyglet
from space_object import SpaceObject

MAX_SPEED = 100     # pixels per second
ACCELERATION = 50
ROTATION_SPEED = 4  # radians per second

class Spaceship(SpaceObject):
    
    def __init__(self, window_width, window_height, batch):
        super().__init__(window_width // 2, window_height // 2, 0, window_width, window_height)
        # sprite
        image = pyglet.image.load('images/playerShip1_blue.png')
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        self.sprite = pyglet.sprite.Sprite(image, batch=batch)
        
        # speed
        self.x_speed = 0    # pixels per second
        self.y_speed = 0    # pixels per second
        
        # sprite position
        self.sync_sprite()
        
        
    def sync_sprite(self):
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.rotation = 90 - math.degrees(self.rotation)  # degrees
        
    
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
        self.sync_sprite()
        