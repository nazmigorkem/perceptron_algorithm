import numpy as np
from plot import Plot

class Base:
    def find_error(w, target_function, size = 10000):
            x = np.random.uniform(-1, 1, size)
            y = np.random.uniform(-1, 1, size)
            count = 0
            plot = Plot()
            for (xi, yi) in zip(x, y):
                if (plot.is_above_line(xi, yi, w) != plot.is_above_line(xi, yi, target_function)):
                    count += 1

            return count / size

    def ein(w, target_function, x, y, size = 1000):
            count = 0
            plot = Plot()
            for (xi, yi) in zip(x, y):
                if (plot.is_above_line(xi, yi, w) != plot.is_above_line(xi, yi, target_function)):
                    count += 1

            return count / size
