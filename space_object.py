# Class for each space object

import math
import pyglet


class SpaceObject:
    ''' Superclass for space objects'''
    
    def __init__(self, x, y, rotation, window_width, window_height, image_path, batch):
        self.x = x
        self.y = y
        self.x_speed = 0    # pixels per second
        self.y_speed = 0    # pixels per second
        self.rotation = rotation   # in radians
        # space dimensions
        self.space_width = window_width
        self.space_height = window_height
        # sprite
        image = pyglet.image.load(image_path)
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        self.sprite = pyglet.sprite.Sprite(image, batch=batch)
        # sprite position
        self.sync_sprite()
    

    def sync_sprite(self):
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.rotation = 90 - math.degrees(self.rotation)  # degrees


    def tick(self, dt):
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
        