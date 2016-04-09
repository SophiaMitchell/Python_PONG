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

def calc_intercept(obj1, obj2):
    """ Calculates where object 1's trajectory will intercept object 
    2's y-axis"""
    x = obj1.x
    y = obj1.y
    vx = obj1.v_x
    vy = obj1.v_y  
    max_y = config.upper_y_bound
    
    # The x position of object 2's y-axis
    y_ax = obj2.x

    # Now simply calculate where the ball will intercept the axis
    m = vy/vx
    b = y-(m*x)
    yint = (m*y_ax) + b
    
    # If this is above or below the game area, the ball will be 
    # bouncing. Iteratively figure out where the ball is bouncing   
    # and determine where the ball will intercept object 2's y-axis 
    # within the game area.
    while (yint < 0 or yint > max_y):
        inf_loop = 0 

        if yint < 0:
            x = (0-b)/m
            m = -m
            b = 0-(m*x)
            yint = (m*y_ax) + b
        else:
            x = (max_y-b)/m       
            m = -m
            b = max_y-(m*x)
            yint = (m*y_ax) + b
        
        # Seriously if there are more than 100 bounces then you need
        # to calm down your bounce game. So if this loop runs more 
        # than 40 times we're calling it quits.
        if inf_loop > 100:
            break 

        inf_loop += 1
        
    return yint
