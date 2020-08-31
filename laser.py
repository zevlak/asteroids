# Class for laser fired by spaceship

import math
from space_object import SpaceObject


LASER_LIVE = 2      # in seconds
LASER_SPEED = 500   # pixels per second


class Laser(SpaceObject):
    
    def __init__(self, x, y, rotation, sprite, ship_x_speed, ship_y_speed, space_width, space_height):
        super().__init__(x, y, rotation, sprite, space_width, space_height)
        
        self.x_speed += LASER_SPEED * math.cos(self.rotation) + ship_x_speed
        self.y_speed += LASER_SPEED * math.sin(self.rotation) + ship_y_speed
        self.life_time = LASER_LIVE

    def live(self):
        '''If laser lives then return True'''
        return self.life_time > 0
    
    def tick(self, dt):
        super().tick(dt)
        
        self.life_time -= dt
