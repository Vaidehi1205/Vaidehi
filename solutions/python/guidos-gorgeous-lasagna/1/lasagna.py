"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

EXPECTED_BAKE_TIME=40
PREPARATION_TIME=2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.


    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.

def preparation_time_in_minutes(number_of_layers):

    """Calculate preparation time based on layers.

    :param number_of_layers: int - number of lasagna layers to prepare.
    :return: int - total preparation time (in minutes).

    Given the number of layers, this function returns how many minutes it will
    take to prepare them. Each layer takes PREPARATION_TIME minutes to add.
    """
    
    return number_of_layers*PREPARATION_TIME
    
#TODO: define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers ,elapsed_bake_time ):
    """Calculate the total time spent cooking.

    :param number_of_layers: int - number of layers added to the lasagna.
    :param elapsed_bake_time: int - elapsed baking time (in minutes).
    :return: int - total time spent preparing and baking the lasagna.

    This function calculates the total time spent in the kitchen by summing
    the preparation time (based on layers) and the baking time so far.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)

print(EXPECTED_BAKE_TIME)
bake_time_remaining(30)
preparation_time_in_minutes(2)
elapsed_time_in_minutes(3, 20)

