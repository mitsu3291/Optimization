import cvxpy
import numpy as np

if __name__ == "__main__":
    # define variable
    A = np.array([[3,2],[2,6]])
    b = np.array([5,8])
    c = np.array([2,3])

    # define and solve LP problem
    x = cvxpy.Variable(2) # dimention of decision variable
    objective = cvxpy.Minimize(c.T@x) # objective function
    constraints = [A@x >= b,
                   x >= 0]
    prob = cvxpy.Problem(objective, constraints)
    prob.solve()

    # show result
    print("The optimal value is", prob.value)
    print("A solution x is") 
    print(x.value)
    print("A dual solution is")
    print(prob.constraints[0].dual_value)