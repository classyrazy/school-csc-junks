'''    Write a function my_cubic_spline(x, y, X) where x and y are 
    arrays that contain experimental data points,
    and X is an array. Assume that x and X are in ascending 
    order and have unique elements. The output argument ,Y,
    should be an array the same size as X,
    where Y[i] is cubic spline interpolation of X[i] 
    do not use interp1d or cubic spline '''

import numpy as np
import matplotlib.pyplot as plt


def cubic_spline_interpolation(x_data, y_data, x_query):
    # Determine the number of input points
    num_points = len(x_data)

    # Compute the coefficients of the cubic polynomials for each interval between adjacent input points
    a = y_data[:-1]  # Constant coefficient of each cubic polynomial
    b = np.diff(y_data) / np.diff(x_data)  # Linear coefficient of each cubic polynomial
    c = np.zeros(num_points-1)
    d = np.zeros(num_points-1) 

    for i in range(num_points-1):
        # Compute the coefficients of the i-th cubic polynomial
        c[i] = 3*b[i] - 2*a[i] - b[i]*np.diff(x_data)[i]
        d[i] = 2*a[i] - 3*b[i] + b[i]*np.diff(x_data)[i]

    # Interpolate the values at the query points
    interpolated_y = np.zeros(len(x_query))
    j = 0
    for i in range(len(x_query)):
        # Find the index of the interval containing the i-th query point
        while j < num_points-2 and x_query[i] > x_data[j+1]:
            j += 1

        # Compute the interpolated value at the i-th query point using the cubic polynomial for its interval
        t = (x_query[i] - x_data[j]) / np.diff(x_data)[j]
        interpolated_y[i] = a[j] + b[j]*t + c[j]*t**2 + d[j]*t**3

    return interpolated_y


# Define the input data
x_data = np.array([0, 1, 2])  # x-coordinates of the input points
y_data = np.array([1, 3, 2])  # y-coordinates of the input points

# Define the query points
x_query = np.linspace(0, 5, 101)

# Compute the interpolated values
interpolated_y = cubic_spline_interpolation(x_data, y_data, x_query)

# Plot the data and the interpolation
plt.plot(x_data, y_data, 'r', label='Input Data')
plt.plot(x_query, interpolated_y, label='cubic spline interpolation')
plt.legend()
plt.show()
