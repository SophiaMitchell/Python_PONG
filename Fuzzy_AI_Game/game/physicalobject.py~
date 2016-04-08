import pyglet
import util

class PhysicalObject(pyglet.sprite.Sprite):
    """A sprite with physical properties such as velocity"""

    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        self.v_x, self.v_y = 0.0,0.0
        self.is_ball = False

        self.new_objects = []
        self.event_handlers = []

    def update(self, dt):
        self.x += self.v_x * dt
        self.y += self.v_y * dt

        self.check_bounds()

    def check_bounds(self):

        min_x = 0
        min_y = 0
        max_x = 1000 - self.image.width
        max_y = 550 - self.image.height

        if self.is_ball:    

            if self.x < min_x:
                util.score(self, 1)
            elif self.x > max_x:
                util.score(self, 2)
            if self.y < min_y:
                self.v_y = self.v_y * -1
                self.y = min_y
            elif self.y > max_y:
                self.v_y = self.v_y * -1
                self.y = max_y
               

        else:

            if self.x < min_x:
                self.x = min_x
            elif self.x > max_x:
                self.x = max_x
            if self.y < min_y:
                self.y = min_y
            elif self.y > max_y:
                self.y = max_y

    def collides_with(self, other_object):
        left = self.x
        right = self.x + self.image.width
        bottom = self.y
        top = self.y + self.image.height

        other_left = other_object.x
        other_right = other_object.x + other_object.image.width
        other_bottom = other_object.y
        other_top = other_object.y + other_object.image.height
      
        if left > other_left and left < other_right:
            if top < other_top and bottom > other_bottom:
                return True
            elif top > other_top and bottom < other_top:
                return True
            elif top > other_bottom and bottom < other_bottom:
                return True
        elif right > other_left and right < other_right:
            if top < other_top and bottom > other_bottom:
                return True
            elif top > other_top and bottom < other_top:
                return True
            elif top > other_bottom and bottom < other_bottom:
                return True
        else:
            return False 

