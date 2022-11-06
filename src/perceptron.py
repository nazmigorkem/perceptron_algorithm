from plot import Plot
import numpy as np
import random
from base import Base

class Perceptron:
    def __init__(self):
        pass
    
    def update_weight_vector(self, w: list[float], point: list[float], d, learning_rate: float):
        for i, val in enumerate(w):
            w[i] = val +  learning_rate * d * point[i]

        return w

    def main_loop(self, w, x: list[float], y: list[float], target_function, fig = None, learning_rate: float = 1):
        plot = Plot()
        is_done = False
        iteration_count = 0
        coloring_line = None
        misclassified = []
        zipped = list(zip(x, y))
        while is_done is not True:
            misclassified.clear()
            for (xi, yi) in zipped:
                sign = plot.is_above_line(xi, yi, w)
                is_above = plot.is_above_line(xi, yi, target_function)
                if sign != is_above:
                    misclassified.append((1, xi, yi, is_above))
                
            if (len(misclassified) != 0):
                iteration_count += 1
                is_done = False
                selected = random.choice(misclassified)
                w = self.update_weight_vector(w, selected[:-1], 1 if selected[3] else -1, learning_rate)

                if (w[2] != 0 and fig != None):
                    if coloring_line is not None:
                        coloring_line[0].remove()
                    coloring_line = plot.draw_line(w, color="red")
                    plot.update_drawing(fig)
            else:
                is_done = True

        error = Base.find_error(w, target_function)
        print(f"Perceptron Error: {error} | Found in {iteration_count} iterations")
        return {"iteration_count": iteration_count, "error": error ,"w": w}
