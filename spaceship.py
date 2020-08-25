# Class Spaceship for Asteroids game

import math
import pyglet

MAX_SPEED = 100     # pixels per second
ACCELERATION = 50
ROTATION_SPEED = 4  # radians per second

class Spaceship:
    
    def __init__(self, window_width, window_height, batch):
        # sprite
        image = pyglet.image.load('images/playerShip1_blue.png')
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        self.sprite = pyglet.sprite.Sprite(image, batch=batch)

        # position
        self.x = window_width // 2
        self.y = window_height // 2
        self.rotation = 0   # radians
        
        # speed
        self.x_speed = 0    # pixels per second
        self.y_speed = 0    # pixels per second
        
        # sprite position
        self.sync_sprite()
        
        # space dimensions
        self.space_width = window_width
        self.space_height = window_height
        
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
        
        self.x += dt * self.x_speed
        self.y += dt * self.y_speed
        if self.x < 0:
            self.x = self.space_width
        elif self.x > self.space_width:
            self.x = 0
        if self.y <= 0:
            self.y = self.space_height
        elif self.y >= self.space_height:
            self.y = 0
        self.sync_sprite()
        