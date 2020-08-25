# Class for each space object

class SpaceObject:
    def __init__(self, x, y, rotation, window_width, window_height):
        self.x = x
        self.y = y
        self.x_speed = 0    # pixels per second
        self.y_speed = 0    # pixels per second
        self.rotation = rotation   # in radians
        # space dimensions
        self.space_width = window_width
        self.space_height = window_height
    
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
        