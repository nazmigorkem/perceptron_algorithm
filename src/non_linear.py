import random
import matplotlib.pyplot as plt
from plot import Plot

class NonLinear:
    def generate(self, x, y, fig = None):
        Y = []
        plot = Plot()
        is_blue = False
        for (xi, yi) in zip(x, y):
            is_blue = False
            fnc = xi ** 2 + yi ** 2 - 0.6
            if random.uniform(0, 1) <= 0.1:
                if fnc > 0:
                    Y.append(-1)
                else:
                    is_blue = True
                    Y.append(1)
            else:
                if fnc > 0:
                    is_blue = True
                    Y.append(1)
                else:
                    Y.append(-1)
            if fig != None:
                plt.plot(xi, yi, "o", color="blue" if is_blue else "red")
        
        if fig != None:
            plot.update_drawing(fig)
          
        return Y