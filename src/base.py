import numpy as np
from plot import Plot

class Base:
    def find_error(w, target_function):
            x = np.random.uniform(-1, 1, 10000)
            y = np.random.uniform(-1, 1, 10000)
            w_count = 0
            target_function_count = 0
            plot = Plot()
            for (xi, yi) in zip(x, y):
                if (plot.is_above_line(xi, yi, w)):
                    w_count += 1
                
                if (plot.is_above_line(xi, yi, target_function)):
                    target_function_count += 1

            return abs((target_function_count - w_count) / target_function_count)