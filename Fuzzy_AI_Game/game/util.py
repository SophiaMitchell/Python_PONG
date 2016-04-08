import pyglet, math, random, config

def score(ball, side):
    if side == 1:
        reset_game(ball, 0, 1)
    if side == 2:
        reset_game(ball, 1, 0)

def reset_game(ball, add_pl, add_comp):
    config.pl_score += add_pl
    config.comp_score += add_comp
    ball.x, ball.y = 500, 300    
    a = random.choice([-1,1])
    b = random.choice([-1,1])
    ball.v_x, ball.v_y = random.randint(200,250)*a, random.randint(200,250)*b
    

def distance(point_1 = (0,0), point_2 = (0,0)):
    """Returns the distance between two points"""
    return math.sqrt((point_1[0] - point_2[0])** 2 + (point_1[1] - point_2[1]) ** 2)

