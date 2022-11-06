import numpy as np

class Plot:
    def __init__(self):
        pass

    def construct_function(self, slope, constant):
        return {
            "slope": slope,
            "constant": constant
        }
    
    ### true = above, false = below
    def is_above_target_line(self, x: float, y: float, target_function):
        return y - target_function["slope"] * x - target_function["constant"] > 0