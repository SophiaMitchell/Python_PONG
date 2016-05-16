import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

def game_type(player, comp):
    """ A fuzzy algorithm to define the offensiveness and/or 
    defensiveness of the game. Determines how aggressive the fuzzy 
    player is"""

    score_diff = float(player-comp)
    ### Inputs ###
    # Input Variable Domain
    score = np.arange(-21, 21, .01)
    
    # Input membership functions
    score_ahead = fuzz.gaussmf(score, -21, 8.823)
    score_tied = fuzz.gaussmf(score, 0, 9.012)
    score_behind = fuzz.gaussmf(score, 21, 8.823)

    # Fuzzifying the current input
    def score_category(sc):
        score_cat_ahead = fuzz.interp_membership(score, score_ahead, sc)
        score_cat_tied = fuzz.interp_membership(score, score_tied, sc)
        score_cat_behind = fuzz.interp_membership(score, score_behind, sc)
        return dict(ahead = score_cat_ahead, tied = score_cat_tied, behind = score_cat_behind)

    ### Outputs ###
    # Output Variable Domain
    game = np.arange(-1, 1, .001)

    # Output membership functions
    game_defensive = fuzz.gauss2mf(game, -1.31, .416, 0.09, .162899)
    game_offensive = fuzz.gauss2mf(game, .30291, .090976, 1.31, .416)

    ### Rules ###
    current_score = score_category(score_diff)

    # Going to make this a hard opponent, so if the score is tied or 
    # if the human is winning, it will play offensively
    rule1 = current_score['ahead']
    rule2 = np.fmax(current_score['tied'], current_score['behind'])

    # Apply implication operator (Mamdami)
    imp1 = np.fmin(rule1, game_defensive)
    imp2 = np.fmin(rule2, game_offensive)

    # Aggregate outputs using max
    aggregate_membership = np.fmax(imp1, imp2)

    # Defuzzify using centroid and return the result
    result_game = fuzz.defuzz(game, aggregate_membership, 'centroid')
    return result_game

def move_fuzzy(distance_in):
    """ A simple fuzzy movement algorithm. Hit the ball with the 
    center of the paddle. """

    # Convert the distance from this game's 550 unit tall area to 
    # the 200 unit tall are this fuzzy system was made for in MATLAB
    distance_in = distance_in/2.75

    ### Inputs ###
    # Input variable domain
    dist = np.arange(-200, 200, .01)

    # Input Membership Functions
    far_below = fuzz.gbellmf(dist, 79.68, 24.6, -90)
    close_below = fuzz.gaussmf(dist, -6.57989, 3.17) 
    on_target = fuzz.gaussmf(dist, 0, 2)
    close_above = fuzz.gaussmf(dist, 6.58, 3.17)
    far_above = fuzz.gbellmf(dist, 79.68, 24.6, 90) 

    # Fuzzifying the inputs
    def dist_category(dist_in):
        dist_cat_far_below = fuzz.interp_membership(dist, far_below, dist_in) 
        dist_cat_close_below = fuzz.interp_membership(dist, close_below, dist_in)
        dist_cat_on_target = fuzz.interp_membership(dist, on_target, dist_in)
        dist_cat_close_above = fuzz.interp_membership(dist, close_above, dist_in)
        dist_cat_far_above = fuzz.interp_membership(dist, far_above, dist_in)
        return dict(fbelow = dist_cat_far_below, cbelow = dist_cat_close_below, target = dist_cat_on_target, cabove = dist_cat_close_above, fabove = dist_cat_far_above)

    ### Outputs ###
    # Output Variable Domain
    move = np.arange(-1, 1, .001)

    # Output Membership Functions
    down_fast = fuzz.trapmf(move, [-1.45, -1.05, -0.2, -0.1])
    down_slow = fuzz.trimf(move, [-0.2, -0.1, 0])
    none = fuzz.trimf(move, [-0.1, 0, 0.1])
    up_slow = fuzz.trimf(move, [0, 0.1, 0.2])
    up_fast = fuzz.trapmf(move, [0.1, 0.2, 1.14, 1.38])

    ### Rules ###
    this_move = dist_category(float(distance_in))
    
    rule1 = this_move['fbelow']
    rule2 = this_move['cbelow']
    rule3 = this_move['target']
    rule4 = this_move['cabove']
    rule5 = this_move['fabove']

    # Apply implication operator (Mandami) connecting rules to 
    # output mfs
    imp1 = np.fmin(rule1, down_fast)
    imp2 = np.fmin(rule2, down_slow)
    imp3 = np.fmin(rule3, none)
    imp4 = np.fmin(rule4, up_slow)
    imp5 = np.fmin(rule5, up_fast)

    # Aggregate outputs using max
    agg_memb = np.fmax(imp1, np.fmax(imp2, np.fmax(imp3, np.fmax(imp4, imp5))))
    # Defuzzify using centroid and return the result
    move_result = fuzz.defuzz(move, agg_memb, 'centroid')
    return move_result


