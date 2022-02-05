import matplotlib.pyplot as plt
import numpy as np
from utils import func
from matplotlib.animation import FuncAnimation

class Plotter:
    def __init__(self):
        pass

    def animation(self, x_traj):
        fig = plt.figure()
        ax = fig.add_subplot(111, aspect="equal")
        
        def update(i):
            ax.cla() # ax をクリア
            ax.set_xlim(-4,4)

            # plot f(x)
            x = np.linspace(-3,3,100)
            y = func.f(x)
            ax.plot(x,y)

            # plot x_traj
            ax.scatter(x_traj[i], func.f(x_traj[i]), c="red")

        anim = FuncAnimation(fig, update, frames=range(len(x_traj)), interval=50)
        plt.show()