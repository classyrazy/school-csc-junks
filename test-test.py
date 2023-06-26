# import numpy as np
# import matplotlib.pyplot as plt
# def my_cubic_spline(x, y, X):
#     n = len(x)
#     a = y.copy()
#     b = np.zeros(n)
#     d = np.zeros(n)

#     # Calculate coefficients of natural cubic spline
#     h = x[1:] - x[:-1]
#     alpha = (3 * (a[1:] - a[:-1])) / h
#     c = np.zeros(n+1)
#     l = np.ones(n+1)
#     mu = np.zeros(n+1)
#     z = np.zeros(n+1)

#     for i in range(1, n):
#         l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
#         mu[i] = h[i] / l[i]
#         z[i] = (alpha[i-1] - h[i-1]*z[i-1]) / l[i]

#     for j in range(n-1, 0, -1):
#         c[j] = z[j] - mu[j] * c[j+1]
#         b[j] = (a[j+1] - a[j]) / h[j] - h[j] * (c[j+1] + 2 * c[j]) / 3
#         d[j] = (c[j+1] - c[j]) / (3 * h[j])

#     # Evaluate cubic spline at X
#     Y = np.zeros_like(X)
#     for i in range(len(X)):
#         j = np.searchsorted(x, X[i])
#         if j == 0:
#             j = 1
#         elif j == n:
#             j = n - 1

#         dx = X[i] - x[j]
#         Y[i] = a[j] + b[j] * dx + c[j] * dx**2 + d[j] * dx**3

#     return Y


# # Define the input data
# x = np.array([0, 1, 2])
# y = np.array([1, 3, 2])
# # Define the query points
# X = np.linspace(0, 5, 11)
# # Compute the interpolated values
# Y = my_cubic_spline(x, y, X)
# # Plot the data and the interpolation
# plt.plot(x, y, 'r', label='data')
# plt.plot(X, Y, label='cubic spline interpolation')
# plt.legend()
# plt.show()


def main():
    print("Select a method:")
    print("1. Bisection")
    print("2. Newton-Raphson")
    print("3. Secant")
    
    method = int(input("Enter the method number: "))
    if method not in [1, 2, 3]:
        print("Invalid method selected.")
        return
    equation = input("Equation in the form ax^n + bx + c = 0[i.e - values for a b c n respectively]: ")
    coefficients = [float(x) for x in equation.split()]
    
    if method == 1:
        initial_solutions = [float(x) for x in input("Initial Solutions (r s): ").split()]
        solution = bisection_method(coefficients[0], coefficients[1], coefficients[2], coefficients[3], initial_solutions[0], initial_solutions[1])
    elif method == 2:
        initial_solution = float(input("Initial Solution (r): "))
        solution = newton_raphson_method(coefficients[0], coefficients[1], coefficients[2], coefficients[3], initial_solution)
    elif method == 3:
        initial_solutions = [float(x) for x in input("Initial Solutions (r s): ").split()]
        solution = secant_method(coefficients[0], coefficients[1], coefficients[2], coefficients[3], initial_solutions[0], initial_solutions[1])
    else:
        print("Invalid method selected.")
        return
    
    if solution is not None:
        print(f"The approximate root of {coefficients[0]}x^{coefficients[3]} + {coefficients[1]}x + {coefficients[2]} = 0 is :", solution)
    else:
        print("No solution found.")