# Class Spaceship for Asteroids game

import math
import pyglet
from laser import Laser
from space_object import SpaceObject

ACCELERATION = 50
ROTATION_SPEED = 4      # radians per second
LASER_CADENCE = 0.3     # second to fire
UNBEATEABLE_TIME = 3    # ship cannot been killed in this time after creation

class Spaceship(SpaceObject):
    
    def __init__(self, x, y, sprite, engine_sprite, space_width, space_height):
        self.engine_sprite = engine_sprite
        self.engine_sprite.visible = False
        
        super().__init__(
            x,
            y,
            0,
            sprite,
            space_width,
            space_height
        )
        
        self.unbeatable_time = UNBEATEABLE_TIME
        self.fire_sound = pyglet.media.StaticSource(pyglet.media.load('sounds/laser-gun-19sf.mp3'))
        self.last_fire = 0
    
    def delete(self):
        '''Delete engine sprite too'''
        self.engine_sprite.delete()
        del(self.engine_sprite)
        super().delete()
    
    def fire(self, sprite):
        '''Fires laser if can'''
        if self.last_fire > LASER_CADENCE:
            self.last_fire = 0
            self.fire_sound.play()
            return Laser(self.x, self.y, self.rotation, sprite, self.x_speed, self.y_speed, self.space_width, self.space_height)
        
    def tick(self, dt, pressed_keys):
        '''Move spaceship'''
        # blinks in unbeatable status
        if self.is_unbeatable():
            self.unbeatable_time -= dt
            self.sprite.visible = not self.sprite.visible
        elif not self.sprite.visible:
            self.sprite.visible = True
        
        # rotation
        if pyglet.window.key.LEFT in pressed_keys:
            self.rotation += dt * ROTATION_SPEED
        if pyglet.window.key.RIGHT in pressed_keys:
            self.rotation -= dt * ROTATION_SPEED
       
        # move
        if pyglet.window.key.UP in pressed_keys:
            self.x_speed += dt * ACCELERATION * math.cos(self.rotation)
            self.y_speed += dt * ACCELERATION * math.sin(self.rotation)
            self.engine_sprite.visible = True
        else:
            self.engine_sprite.visible = False
        
        self.last_fire += dt
        
        super().tick(dt)
    
    def sync_sprite(self):
        '''Moves sprite to object location'''
        super().sync_sprite()

        self.engine_sprite.x = self.x
        self.engine_sprite.y = self.y
        self.engine_sprite.rotation = self.sprite.rotation
        
    def is_unbeatable(self):
        '''If ship si unbeatable'''
        return self.unbeatable_time > 0