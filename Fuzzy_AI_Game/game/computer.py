import pyglet, math
from pyglet.window import key
import physicalobject, resources, fuzzpaddle, util

class Computer(physicalobject.PhysicalObject):
    
    def __init__(self, ball_object, *args, **kwargs):
        super(Computer, self).__init__(img=resources.paddle, *args, **kwargs)
        self.thrust = 300.0
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
        
        # Center of the paddle in the y direction
        self.center = self.y + (self.image.height/2)

    def update(self, ball_object, dt):
        super(Computer, self).update(dt)

        # Upadting where the center of the paddle is
        self.center = self.y + (self.image.height/2)     
 
        # Tying the ball information into the computer for
        # situational awareness. This may or may not work... we'll
        # see?
        self.the_ball = ball_object      
 
        # Computer is a lot like player, but instead of using the    
        # key handler to control movement we're using a fuzzy system 
        # from "fuzzpaddle".
        self.v_y = (handle_movement(self, the_ball) * self.thrust) * dt

    def handle_movement(self, the_ball):
        """ Figures out where the ball will be, and then calls the 
        cascading set of fuzzy sysetms to determine where the paddle 
        should go"""
        
        # Figure out where the ball will intercept the paddle's y-
        # axis and then determine how far away the center of the 
        # paddle is from that point.
        yint = util.calc_intercept(the_ball, self)
        difference = self.center - yint
        
        # Now I have the situational awareness needed for the basic 
        # fuzzy controller (just hits the ball, no strategy). Using 
        # the fuzzy systems to determine v_y.                
        game = fuzzpaddle.game_type(config.pl_score, config.comp_score)
        move = fuzzpaddle.move_fuzzy(game, difference)
        return move

