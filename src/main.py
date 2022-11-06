import numpy as np
import sys
from plot import Plot
from perceptron import Perceptron


n = int(sys.argv[1])
loop_count = int(sys.argv[2])


total_iteration_count = 0
iteration_count = 0
total_error = 0
error = 0
plot = Plot()

for i in range(loop_count):
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)
    w = [0, 0, 0]

    random_x = np.random.uniform(-1, 1, 2)
    random_y = np.random.uniform(-1, 1, 2)
    slope = (random_y[1] - random_y[0]) / (random_x[1] - random_x[0])
    c = -slope * random_x[0] + random_y[0]
    target_function = [c, slope, -1]

    print(f"Loop {i+1}: ", end="")
    if (loop_count == 1):
        fig = plot.enable_drawing()

        plot.classify_data(x, y, target_function)
        result = Perceptron().main_loop(w, x, y, target_function, fig)
        iteration_count = result["iteration_count"]
        error = result["error"]
        plot.draw_line(target_function, color="green")

        plot.disable_drawing()
    else:
        result = Perceptron().main_loop(w, x, y, target_function)
        iteration_count = result["iteration_count"]
        error = result["error"]

    total_iteration_count += iteration_count
    total_error += error

print(f"Mean of iteration counts: {total_iteration_count / loop_count} | Mean of errors: {total_error / loop_count}")


