import matplotlib.pyplot as plt
import numpy as np
import sys
from plot import Plot
from perceptron import Perceptron


n = int(sys.argv[1])
loop_count = int(sys.argv[2])


total = 0
iteration_count = 0
for i in range(loop_count):
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)
    w = [0, 0, 0]
    plot = Plot()

    target_function = plot.construct_function(
            (np.random.uniform(-1 , 1) - np.random.uniform(-1 , 1)) / (np.random.uniform(-1 , 1) - np.random.uniform(-1 , 1)), 
            np.random.uniform(-1 , 1)
        )

    print(f"Loop {i+1}: ", end="")
    if (loop_count == 1):
        fig = plot.enable_drawing()

        for (i, (x1, y1)) in enumerate(zip(x, y)):
            plt.plot(x1, y1, "o", color="blue" if plot.is_above_target_line(x1, y1, target_function) else "red")
        
        result = Perceptron().main_loop(w, [x, y], target_function, fig)
        iteration_count = result["iteration_count"]
        
        plot.disable_drawing()
    else:
        result = Perceptron().main_loop(w, [x, y], target_function)
        iteration_count = result["iteration_count"]

    total += iteration_count

print(f"Mean of iterations is {total / loop_count}")


