import matplotlib.pyplot as plt

class Plot:
    def __init__(self):
        pass

    def construct_function(self, slope, constant):
        return {
            "slope": slope,
            "constant": constant
        }
    
    # w2y = - w1x - w0
    def draw_line(self, w, color):
        return plt.plot([-1, 1], [(-w[1] + w[0]) / -w[2], (w[1] + w[0]) / -w[2]], color=color)
    
    ### true = above, false = below
    def is_above_line(self, x: float, y: float, w):
        return w[0] + w[1] * x + w[2] * y > 0

    def classify_data(self, x, y, target_function):
         for (i, (x1, y1)) in enumerate(zip(x, y)):
            plt.plot(x1, y1, "o", color="blue" if self.is_above_line(x1, y1, target_function) else "red")
        

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