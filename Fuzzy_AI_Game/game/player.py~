import pyglet, math
from pyglet.window import key
import physicalobject, resources

class Player(physicalobject.PhysicalObject):
    
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.paddle, *args, **kwargs)
        
        self.thrust = 300.0
        self.score = 0

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

    def update(self, dt):
        super(Player, self).update(dt)
      
        if self.key_handler[key.Q]:
            self.v_y += self.thrust * dt
        elif self.key_handler[key.A]:
            self.v_y -= self.thrust * dt
        else:
            self.v_y = 0

