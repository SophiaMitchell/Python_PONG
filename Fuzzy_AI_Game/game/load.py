import pyglet, math, random
import physicalobject, resources, ball, util, config

def balls(batch=None):
    pong_ball = ball.Ball(x = 500, y=300, batch=batch)
    config.ball = pong_ball
    util.reset_game(pong_ball,0,0)
    return [pong_ball]    

