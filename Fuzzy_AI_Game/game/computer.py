import pyglet, math
from pyglet.window import key
import physicalobject, resources

class Computer(physicalobject.PhysicalObject):
    
    def __init__(self, *args, **kwargs):
        super(Computer, self).__init__(img=resources.paddle, *args, **kwargs)
        
        self.thrust = 300.0

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

    def update(self, dt):
        super(Computer, self).update(dt)
      
        if self.key_handler[key.UP]:
            self.v_y += self.thrust * dt
        elif self.key_handler[key.DOWN]:
            self.v_y -= self.thrust * dt
        else:
            self.v_y = 0
