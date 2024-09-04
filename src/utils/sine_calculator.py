import math

def sine_calculate(base_y, timer, amplitude=5, frequency=0.015):
    """
    Calculate the new y position using a sine wave for smooth movement.
    
    :param base_y: The base y position around which the object will hover.
    :param timer: A timer value to feed into the sine function to simulate time.
    :param amplitude: The maximum distance the object will move from the base y position.
    :param frequency: How fast the object will move up and down (lower values = slower).
    :return: The new y position.
    """
    return base_y + amplitude * math.sin(frequency * timer)




