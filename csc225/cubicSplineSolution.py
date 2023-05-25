'''    Write a function my_cubic_spline(x, y, X) where x and y are 
    arrays that contain experimental data points,
    and X is an array. Assume that x and X are in ascending 
    order and have unique elements. The output argument ,Y,
    should be an array the same size as X,
    where Y[i] is cubic spline interpolation of X[i] 
    do not use interp1d or cubic spline '''

import numpy as np
import matplotlib.pyplot as plt


def my_cubic_spline(x, y, X):
    num_points = len(x)

    # Compute the coefficients of the cubic polynomials
    a = y[:-1]
    b = np.diff(y) / np.diff(x)
    c = np.zeros(num_points-1)
    d = np.zeros(num_points-1)

    for i in range(num_points-1):
        # Compute coefficients of the i-th cubic polynomial
        c[i] = 3*b[i] - 2*a[i] - b[i]*np.diff(x)[i]
        d[i] = 2*a[i] - 3*b[i] + b[i]*np.diff(x)[i]

    # Interpolate the values at the query points
    interpolated_values = np.zeros(len(X))
    j = 0
    for i in range(len(X)):
        # Find the appropriate interval [x[j], x[j+1]] for the i-th query point
        while j < num_points-2 and X[i] > x[j+1]:
            j += 1

        # Compute the interpolated value using the cubic polynomial for interval [x[j], x[j+1]]
        t = (X[i] - x[j]) / np.diff(x)[j]
        interpolated_values[i] = a[j] + b[j]*t + c[j]*t**2 + d[j]*t**3

    return interpolated_values


# Define the input data
x_input = np.array([0, 1, 2])
y_input = np.array([1, 3, 2])

# Define the query points
X_data_points = np.linspace(0, 5, 101)

# Compute the interpolated values
interpolated_values = my_cubic_spline(x_input, y_input, X_data_points)

# Plot the data and the interpolation
plt.plot(x_input, y_input, 'r', label='data')
plt.plot(X_data_points, interpolated_values, label='cubic spline interpolation')
plt.legend()
plt.show()
