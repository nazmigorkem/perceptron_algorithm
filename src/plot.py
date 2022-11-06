import matplotlib.pyplot as plt

class Plot:
    def __init__(self):
        pass

    def construct_function(self, slope, constant):
        return {
            "slope": slope,
            "constant": constant
        }
    
    ### true = above, false = below
    def is_above_target_line(self, x: float, y: float, target_function):
        return y - target_function["slope"] * x - target_function["constant"] > 0

    def classify_data(self, x, y, target_function):
         for (i, (x1, y1)) in enumerate(zip(x, y)):
            plt.plot(x1, y1, "o", color="blue" if self.is_above_target_line(x1, y1, target_function) else "red")
        

    def enable_drawing(self):
        plt.ion()
        fig = plt.figure()
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)
        return fig

    def disable_drawing(self):
        plt.ioff()
        plt.show()

    def update_drawing(self, fig):
        fig.canvas.draw()
        fig.canvas.flush_events()