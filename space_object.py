# Class for each space object

import math
import pyglet


class SpaceObject:
    ''' Superclass for space objects'''
    
    def __init__(self, x, y, rotation, sprite, space_width, space_height):
        self.x = x
        self.y = y
        self.x_speed = 0                    # pixels per second
        self.y_speed = 0                    # pixels per second
        self.rotation = rotation            # in radians
        self.space_width = space_width      # pixels
        self.space_height = space_height    # pixels
        self.sprite = sprite
        # sprite position
        self.sync_sprite()
        
        # radius for circle for colision system
        self.radius = self.sprite.width // 2
        
        
    def delete(self):
        '''Delete space object'''
        self.sprite.delete()
        del(self.sprite)
        del(self)
    
    
    def sync_sprite(self):
        '''Moves sprite to object location'''
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.rotation = 90 - math.degrees(self.rotation)  # degrees


    def tick(self, dt):
        '''Moves space object'''
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
    
    def overlaps(self, space_object, space_width, space_height):
        """Returns true if overlaps with another space objects"""
        distance_squared = (distance(self.x, space_object.x, space_width) ** 2 +
                            distance(self.y, space_object.y, space_height) ** 2)
        max_distance_squared = (self.radius + space_object.radius) ** 2
        return distance_squared < max_distance_squared

def distance(a, b, wrap_size):
    """Distance in one direction (x or y)"""
    result = abs(a - b)
    if result > wrap_size / 2:
        result = wrap_size - result
    return result
