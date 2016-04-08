import pyglet
import physicalobject, resources

class Ball(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super(Ball,self).__init__(resources.ball, *args, **kwargs)     
   
        self.is_ball = True
    
    def update(self, dt):
        super(Ball, self).update(dt)

    def handle_hit(self, other_paddle):
        self.v_x = -self.v_x
        paddle_center = other_paddle.y + (other_paddle.image.height/2)
        ball_center = self.y + (self.image.height/2)
        
        self.v_y = (ball_center - paddle_center) * 5
