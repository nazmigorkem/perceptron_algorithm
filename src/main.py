import numpy as np
import sys
from plot import Plot
from perceptron import Perceptron
from linear_regression import LinearRegression

if len(sys.argv) < 4:
    print(f"Please execute the file with following format => py ./path/to/main.py <N> <loop_count> <perceptron | linear_reg | both>")
    print(f"Example => py ./path/to/main.py 100 1000 perceptron")
    exit()

n = int(sys.argv[1])
loop_count = int(sys.argv[2])
algorithm = sys.argv[3]

is_perceptron = algorithm == "perceptron"
is_linear_reg = algorithm == "linear_reg"
is_both = algorithm == "both"

total_iteration_count = 0
iteration_count = 0
total_perceptron_error = 0
total_linear_reg_error = 0
perceptron_error = 0
linear_reg_error = 0
plot = Plot()
x = np.random.uniform(-1, 1, n)
y = np.random.uniform(-1, 1, n)

for i in range(loop_count):
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)
    w = [0, 0, 0]

    random_x = np.random.uniform(-1, 1, 2)
    random_y = np.random.uniform(-1, 1, 2)
    slope = (random_y[1] - random_y[0]) / (random_x[1] - random_x[0])
    c = -slope * random_x[0] + random_y[0]
    target_function = [c, slope, -1]
    
    # if loop count is 1 visualize
    if (loop_count == 1):
        fig = plot.enable_drawing()

        plot.classify_data(x, y, target_function)

        if is_perceptron:
            result_perceptron = Perceptron().main_loop(w, x, y, target_function, fig)
            iteration_count = result_perceptron["iteration_count"]
            perceptron_error = result_perceptron["error"]
        
        elif is_linear_reg:
            result_linear_reg = LinearRegression().get_initial_weigths(x, y, target_function, fig)
            linear_reg_error = result_linear_reg["error"]
        
        else:
            result_linear_reg = LinearRegression().get_initial_weigths(x, y, target_function, fig)
            w = result_linear_reg["w"]
            result_perceptron = Perceptron().main_loop(w, x, y, target_function, fig, 0.1)
            iteration_count = result_perceptron["iteration_count"]
            perceptron_error = result_perceptron["error"]
            linear_reg_error = result_linear_reg["error"]
        
        plot.draw_line(target_function, color="green")
        plot.disable_drawing()

    else:
        print(f"Iteration {i+1}: ", end="")
        if is_perceptron:
            result_perceptron = Perceptron().main_loop(w, x, y, target_function)
            iteration_count = result_perceptron["iteration_count"]
            perceptron_error = result_perceptron["error"]

        elif is_linear_reg:
            result_linear_reg = LinearRegression().get_initial_weigths(x, y, target_function)
            linear_reg_error = result_linear_reg["error"]
        
        else:
            result_linear_reg = LinearRegression().get_initial_weigths(x, y, target_function)
            w = result_linear_reg["w"]
            print(f"Iteration {i+1}: ", end="")
            result_perceptron = Perceptron().main_loop(w, x, y, target_function, learning_rate=0.1)
            iteration_count = result_perceptron["iteration_count"]
            perceptron_error = result_perceptron["error"]
            linear_reg_error = result_linear_reg["error"]


    total_iteration_count += iteration_count
    total_perceptron_error += perceptron_error
    total_linear_reg_error += linear_reg_error

if is_perceptron:
    print(f"Mean of iteration counts: {total_iteration_count / loop_count} | Mean of errors: {total_perceptron_error / loop_count}")
elif is_linear_reg:
    print(f"Mean of errors: {total_perceptron_error / loop_count}")
else:
    print(f"Mean of iteration counts: {total_iteration_count / loop_count} | Mean of perceptron errors: {total_perceptron_error / loop_count} | Mean of perceptron errors: {total_linear_reg_error / loop_count}")
