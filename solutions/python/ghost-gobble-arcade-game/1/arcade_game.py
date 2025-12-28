def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    return (not power_pellet_active) and touching_ghost


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):

    # If Pac-Man loses, he cannot win
    if lose(power_pellet_active, touching_ghost):
        return False

    # Win only if all dots eaten
    return has_eaten_all_dots
