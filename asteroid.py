# Class Asteroid for Asteroids game

from math import pi
import pyglet
from random import choice, randrange, uniform
from space_object import SpaceObject

MAX_SPEED = 100
MAX_ROTATION = 5
IMAGES = [
    'images/meteorGrey_big1.png',
    'images/meteorGrey_big2.png',
    'images/meteorGrey_big3.png',
    'images/meteorGrey_big4.png',
    'images/meteorGrey_med1.png',
    'images/meteorGrey_med2.png',
    'images/meteorGrey_small1.png',
    'images/meteorGrey_small2.png',
    'images/meteorGrey_tiny1.png',
    'images/meteorGrey_tiny2.png',
]


class Asteroid(SpaceObject):
    
    def __init__(self, window_width, window_height, batch):
        '''Parameter batch is pyglet batch for sprites loading'''
        x = 0
        y = 0
        if randrange(0, 2) == 0:
            x = randrange(0, window_width)
        else:
            y = randrange(0, window_height)
        
        super().__init__(
            x,
            y,
            uniform(0,2 * pi),
            window_width,
            window_height,
            choice(IMAGES),
            batch
        )
        
        self.x_speed = randrange(-MAX_SPEED, MAX_SPEED)
        self.y_speed = randrange(-MAX_SPEED, MAX_SPEED)
        self.rotation_speed = uniform(-MAX_ROTATION, MAX_ROTATION)

    
    def tick(self, dt, pressed_keys):
        '''Controls rotation a movement of asteroid'''
        self.rotation += dt * self.rotation_speed
        super().tick(dt)