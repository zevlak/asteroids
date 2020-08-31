# Class Spaceship for Asteroids game

import math
import pyglet
from laser import Laser
from space_object import SpaceObject

ACCELERATION = 50
ROTATION_SPEED = 4  # radians per second
LASER_CADENCE = 0.3   # second to fire

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
        
        self.fire_sound = pyglet.media.StaticSource(pyglet.media.load('sounds/laser-gun-19sf.mp3'))
        self.last_fire = 0
    
    def fire(self, sprite):
        '''Fires laser if can'''
        if self.last_fire > LASER_CADENCE:
            self.last_fire = 0
            self.fire_sound.play()
            return Laser(self.x, self.y, self.rotation, sprite, self.x_speed, self.y_speed, self.space_width, self.space_height)
        
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
        
        self.last_fire += dt
        
        super().tick(dt)
        