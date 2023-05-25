import numpy as np
import matplotlib.pyplot as plt


def my_cubic_spline(x, y, X):
    n = len(x)
    a = y[:-1]
    b = np.diff(y) / np.diff(x)
    c = np.zeros(n-1)
    d = np.zeros(n-1)

    # Compute the coefficients of the cubic polynomials
    for i in range(n-1):
        c[i] = 3*b[i] - 2*a[i] - b[i]*np.diff(x)[i]
        d[i] = 2*a[i] - 3*b[i] + b[i]*np.diff(x)[i]

    # Interpolate the values at the query points
    Y = np.zeros(len(X))
    j = 0
    for i in range(len(X)):
        while j < n-2 and X[i] > x[j+1]:
            j += 1
        t = (X[i] - x[j]) / np.diff(x)[j]
        Y[i] = a[j] + b[j]*t + c[j]*t**2 + d[j]*t**3
    return Y


# Define the input data
x = np.array( [0, 1, 2])
y = np.array([1, 3, 2])
# Define the query points
X = np.linspace(0, 5, 101)
# Compute the interpolated values
Y = my_cubic_spline(x, y, X)
# Plot the data and the interpolation
plt.plot(x, y, 'r', label='data')
# plt.plot(X, Y, label='cubic spline interpolation')
plt.legend()
plt.show()
