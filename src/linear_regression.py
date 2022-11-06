import numpy as np
from plot import Plot
from base import Base

class LinearRegression:
    def __init__(self):
        pass
    
    def get_initial_weigths(self, x, y, target_function, size, fig = None):
        plot = Plot()
        zipped = [list(a) for a in zip([1] * len(x),x, y)]
        Y = []
        for i in zipped:
            Y.append(1 if plot.is_above_line(i[1], i[2], target_function) else -1)
        w = np.dot(np.linalg.pinv(zipped), Y)
        if fig != None:
            plot.update_drawing(fig)
            plot.draw_line(w, "yellow")
        eout = Base.find_error(w, target_function, 1000)
        ein = Base.ein(w, target_function, x, y, size)
        print(f"Linear Reg E_out: {eout} | E_in: {ein}")
        return {"w": w, "error": (eout, ein)}