import numpy as np
from plot import Plot
from base import Base

class LinearRegression:
    def __init__(self):
        pass
    
    def get_initial_weigths(self, x, y, target_function, fig = None):
        plot = Plot()
        zipped = [list(a) for a in zip([1] * len(x),x, y)]
        Y = []
        for i in zipped:
            Y.append(1 if plot.is_above_line(i[1], i[2], target_function) else -1)
        w = np.dot(np.linalg.pinv(zipped), Y)
        if fig != None:
            plot.update_drawing(fig)
            plot.draw_line(w, "yellow")
        error = Base.find_error(w, target_function) ** 2
        print(f"Linear Reg Error: {error}")
        return {"w": w, "error": error}