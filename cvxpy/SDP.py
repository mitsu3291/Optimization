import cvxpy
import numpy as np

if __name__ == "__main__":
    # define variable
    n = 3 # size of X
    p = 2 # num of constraints

    C = np.array([[1, 2, 3],
              [2, 9, 0],
              [3, 0, 7]])
              
    A = []
    A.append(np.array([[1, 0, 1],[0, 3, 7],[1, 7, 5]]))
    A.append(np.array([[0, 2, 8],[2, 6, 0],[8, 0, 4]]))
    print(A)
    
    b = [11,19]

    # Define and solve the CVXPY problem.
    # Create a symmetric matrix variable.
    X = cvxpy.Variable((n,n), symmetric=True)
    # Define the objective and constraints
    objective = cvxpy.Minimize(cvxpy.trace(C@X))
    constraints = []
    constraints = [X >> 0] # The operator >> denotes matrix inequality.
    constraints += [cvxpy.trace(A[i]@X) == b[i] for i in range(p)]
    prob = cvxpy.Problem(objective, constraints)
    prob.solve()
    
    # Print result.
    print("The optimal value is", prob.value)
    print("A solution X is")
    print(X.value)