import numpy as np
import matplotlib.pyplot as plt


def cubic_spline_interpolation(x, y, X):
    num_points = len(x)

    # Compute the coefficients of the cubic polynomials
    a = y[:-1]
    b = np.diff(y) / np.diff(x)
    c = np.zeros(num_points-1)
    d = np.zeros(num_points-1)

    for i in range(num_points-1):
        # Compute the coefficients of the i-th cubic polynomial
        c[i] = 3*b[i] - 2*a[i] - b[i]*np.diff(x)[i]
        d[i] = 2*a[i] - 3*b[i] + b[i]*np.diff(x)[i]

    # Interpolate the values at the query points
    interpolated_y = np.zeros(len(X))
    j = 0
    for i in range(len(X)):
        # Find the appropriate interval [x[j], x[j+1]] for the i-th query point
        while j < num_points-2 and X[i] > x[j+1]:
            j += 1
        t = (X[i] - x[j]) / np.diff(x)[j]
        interpolated_y[i] = a[j] + b[j]*t + c[j]*t**2 + d[j]*t**3

    return interpolated_y


# Define the input data
x = np.array([0, 1, 2])
y = np.array([1, 3, 2])

# Define the query points
X = np.linspace(0, 5, 101)

# Compute the interpolated values
interpolated_y = cubic_spline_interpolation(x, y, X)

# Plot the data and the interpolation
plt.plot(x, y, 'r', label='data')
plt.plot(X, interpolated_y, label='cubic spline interpolation')
plt.legend()
plt.show()
