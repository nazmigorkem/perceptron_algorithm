from plot import Plot
import matplotlib.pyplot as plt
import random

class Perceptron:
    def __init__(self):
        pass
    
    def update_weight_vector(self, w: list[float], point: list[float], d):
        for i, val in enumerate(w):
            w[i] = val + d * point[i]

        return w

    def main_loop(self, w, points: list[list[float]], target_function, fig = None):
        plot = Plot()
        sign = False
        is_done = False
        iteration_count = 0
        coloring_line = None
        while is_done is not True:
            misclassified = []
            x = points[0]
            y = points[1]
            for (x, y) in zip(x, y):
                sign = (w[0] + w[1] * x + w[2] * y) > 0
                is_above = plot.is_above_target_line(x, y, target_function)
                if sign != is_above:
                    misclassified.append((1, x, y, is_above))
                
            if (len(misclassified) != 0):
                iteration_count += 1
                is_done = False
                selected = random.choice(misclassified)
                w = self.update_weight_vector(w, selected[:-1], 1 if selected[3] else -1)

                # w2y = -w1x - w0
                if (w[2] != 0 and fig != None):
                    if coloring_line is not None:
                        coloring_line[0].remove()
                    coloring_line = plt.plot([-1, 1], [(-w[1] + w[0]) / -w[2], (w[1] + w[0]) / -w[2]], color="red")
                    plot.update_drawing(fig)
            else:
                is_done = True

        print(f"Found in {iteration_count} iterations")
        return {"iteration_count": iteration_count, "w": w}