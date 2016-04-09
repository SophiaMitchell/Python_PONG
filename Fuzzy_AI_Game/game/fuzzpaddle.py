import numpy as np
import skfuzzy as fuzz

def game_type(player, comp):
    score_diff = float(player-comp)
    ### Inputs ###
    # Input Variable Domain
    score = np.arange(-21, 21, 1)
    
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
    game = np.arange(0, 1, 1)

    # Output membership functions
    game_defensive = fuzz.gaussmf(game, 0, 0.162899)
    game_offensive = fuzz.gauss2mf(game, 0.30291, 0.090976, 1.31, 0.416)

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

def move_fuzzy(distance):
    ### Inputs ###
    # Input variable domain
    dist = np.arange(-276, 276, 1)

    # Input Membership Functions
    far_below = fuzzy.gbellmf(dist, 79.68, 24.6, -90)
    close_below = fuzzy.gaussmf(dist, -6.57989, 3.17) 
    on_target = fuzzy.gaussmf(dist, 0, 2)
    close_above = fuzzy.gaussmf(dist, 6.58, 3.17)
    far_above = fuzzy.gbellmf(dist, 79.68, 24.6, 90) 

