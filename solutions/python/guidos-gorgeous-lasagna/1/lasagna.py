"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
TIME_PER_LAYER = 2

def bake_time_remaining(elapsed_bake_time: int) -> int:

    """Calculate the expected bake time time in minutes.
        
        Parameters:
            expected_bake_time (int): The expected baking time.
        
        Returns:
            int: The baking time remaining (in minutes)

        This function takes one integer representing the elapsed_baking time. 
        It calculates the baking time remaining
        
        """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

    
def preparation_time_in_minutes(number_of_layers: int):

    """Calculate the preparation time in minutes.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.

    Returns:
        int: The preparation time  (in minutes) 

    This function takes one integer representing the number of lasagna 
    layers . It calculates the total elapsed minutes spent preparing .

    """

    return number_of_layers * TIME_PER_LAYER


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:

    """Calculate the elapsed cooking time.
        
        Parameters:
            number_of_layers (int): The number of layers in the lasagna.
            elapsed_bake_time (int): Time the lasagna has been baking in the oven.
        
        Returns:
            int: The total time elapsed (in minutes) preparing and baking.

        This function takes two integers representing the number of lasagna 
        layers and the time already spent baking the lasagna. It calculates 
        the total elapsed minutes spent cooking (preparing + baking).
        
        """

    return elapsed_bake_time + (number_of_layers * TIME_PER_LAYER)



