from struct import iter_unpack
import matplotlib.pyplot as plt
import numpy as np
from utils.plotter import Plotter
from utils import func

class GradientSteepest:
    def __init__(self):
        self.iter_max = 1000
        self.eps = 1e-4
        self.alpha = 1e-2
        self.is_succeed = False
        self.x_traj = []

    def solve(self, initial_guess):
        x = initial_guess
        for _ in range(1, self.iter_max):
            self.x_traj.append(x)
            x -= self.alpha*func.df(x)
            if abs(func.df(x)) < self.eps:
                self.is_succeed = True
                break

        if self.is_succeed:
            print("Convergence Succeeded!")

        return x

if __name__ == "__main__":
    gs = GradientSteepest()
    solution = gs.solve(initial_guess=2)
    print(f"Solution : {solution}")

    plotter = Plotter()
    plotter.animation(x_traj=gs.x_traj)
    print(f"iteration : {len(gs.x_traj)}")