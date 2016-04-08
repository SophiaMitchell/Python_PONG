import pyglet, math, random
import physicalobject, resources, ball, util

def balls(batch=None):
    pong_ball = ball.Ball(x = 500, y=300, batch=batch)
    util.reset_game(pong_ball,0,0)
    return [pong_ball]    

