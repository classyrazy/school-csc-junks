import time

def bisection_method(func, a, b, epsilon, max_iterations):
    """
    Implements the bisection method to find the root of a function.

    Arguments:
    func -- The function for which the root needs to be found.
    a, b -- The interval [a, b] in which to search for the root.
    epsilon -- The desired accuracy.
    max_iterations -- Maximum number of iterations allowed.

    Returns:
    root -- The estimated root of the function.
    """

    # Initialize iteration counter
    iterations = 0

    # Start timing
    start_time = time.time()

    # Check if the function has opposite signs at the endpoints of the interval
    if func(a) * func(b) >= 0:
        print("Function has the same sign at the endpoints. Bisection method cannot guarantee convergence.")
        return None

    # Iterate until the desired accuracy is achieved or the maximum iterations are reached
    while abs(b - a) > epsilon and iterations < max_iterations:
        # Calculate the midpoint of the interval
        c = (a + b) / 2

        # Check if the midpoint is the root
        if func(c) == 0:
            break

        # Update the interval based on the sign of the function at the midpoint
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c

        # Increment the iteration counter
        iterations += 1

    # Check if the method converged within the maximum iterations
    if iterations == max_iterations:
        print("Maximum iterations reached. The method did not converge.")

    # Calculate elapsed time
    elapsed_time = time.time() - start_time

    # Return the estimated root
    return c, elapsed_time


def newton_raphson_method(func, derivative, x0, epsilon, max_iterations):
    """
    Implements the Newton-Raphson method to find the root of a function.

    Arguments:
    func -- The function for which the root needs to be found.
    derivative -- The derivative of the function.
    x0 -- Initial guess for the root.
    epsilon -- The desired accuracy.
    max_iterations -- Maximum number of iterations allowed.

    Returns:
    root -- The estimated root of the function.
    """

    # Initialize iteration counter and the current approximation
    iterations = 0
    x_curr = x0

    # Start timing
    start_time = time.time()

    # Iterate until the desired accuracy is achieved or the maximum iterations are reached
    while abs(func(x_curr)) > epsilon and iterations < max_iterations:
        # Calculate the next approximation using the Newton-Raphson method formula
        x_next = x_curr - func(x_curr) / derivative(x_curr)

        # Update the current approximation
        x_curr = x_next

        # Increment the iteration counter
        iterations += 1

    # Check if the method converged within the maximum iterations
    if iterations == max_iterations:
        print("Maximum iterations reached. The method did not converge.")

    # Calculate elapsed time
    elapsed_time = time.time() - start_time

    # Return the estimated root
    return x_curr, elapsed_time


def secant_method(func, x0, x1, epsilon, max_iterations):
    """
    Implements the secant method to find the root of a function.

    Arguments:
    func -- The function for which the root needs to be found.
    x0, x1 -- Initial guesses for the root.
    epsilon -- The desired accuracy.
    max_iterations -- Maximum number of iterations allowed.

    Returns:
    root -- The estimated root of the function.
    """

    # Initialize iteration counter and the current and previous approximations
    iterations = 0
    x_curr = x1
    x_prev = x0

    # Start timing
    start_time = time.time()

    # Iterate until the desired accuracy is achieved or the maximum iterations are reached
    while abs(func(x_curr)) > epsilon and iterations < max_iterations:
        # Calculate the next approximation using the secant method formula
        x_next = x_curr - (func(x_curr) * (x_curr - x_prev)) / (func(x_curr) - func(x_prev))

        # Update the current and previous approximations
        x_prev = x_curr
        x_curr = x_next

        # Increment the iteration counter
        iterations += 1

    # Check if the method converged within the maximum iterations
    if iterations == max_iterations:
        print("Maximum iterations reached. The method did not converge.")

    # Calculate elapsed time
    elapsed_time = time.time() - start_time

    # Return the estimated root
    return x_curr, elapsed_time


def taylor_series_method(func, derivative, x0, y0, x, n):
    """
    Implements the Taylor series method to solve an ordinary differential equation.

    Arguments:
    func -- The function representing the derivative of y with respect to x.
    derivative -- The derivative of the function with respect to y.
    x0 -- Initial value of x.
    y0 -- Initial value of y.
    x -- Value of x at which to estimate y.
    n -- The number of terms to consider in the Taylor series.

    Returns:
    y -- The estimated value of y at x.
    """

    # Initialize y to the initial value
    y = y0

    # Calculate the step size
    h = (x - x0) / n

    # Iterate n times to approximate y at x
    for _ in range(n):
        # Calculate the next term in the Taylor series
        dy = func(x0, y) * h

        # Update y by adding the next term
        y += dy

        # Update x0 for the next iteration
        x0 += h

    # Return the estimated value of y at x
    return y


def picard_method(func, x0, y0, x, n):
    """
    Implements the Picard's method to solve an ordinary differential equation.

    Arguments:
    func -- The function representing the derivative of y with respect to x.
    x0 -- Initial value of x.
    y0 -- Initial value of y.
    x -- Value of x at which to estimate y.
    n -- The number of iterations to perform.

    Returns:
    y -- The estimated value of y at x.
    """

    # Initialize y to the initial value
    y = y0

    # Iterate n times to approximate y at x
    for _ in range(n):
        # Calculate the next value of y using the function
        y = func(x0, y)

        # Update x0 for the next iteration
        x0 = x

    # Return the estimated value of y at x
    return y


def euler_method(func, x0, y0, x, n):
    """
    Implements Euler's method to solve an ordinary differential equation.

    Arguments:
    func -- The function representing the derivative of y with respect to x.
    x0 -- Initial value of x.
    y0 -- Initial value of y.
    x -- Value of x at which to estimate y.
    n -- The number of iterations to perform.

    Returns:
    y -- The estimated value of y at x.
    """

    # Initialize y to the initial value
    y = y0

    # Calculate the step size
    h = (x - x0) / n

    # Iterate n times to approximate y at x
    for _ in range(n):
        # Calculate the derivative at the current point
        dy = func(x0, y)

        # Update y using Euler's method
        y += dy * h

        # Update x0 for the next iteration
        x0 += h

    # Return the estimated value of y at x
    return y


# Prompt the user to choose an option
print("Please choose an option:")
print("1. Find the root of an equation")
print("2. Solve an ordinary differential equation")

option = int(input("Enter your choice (1 or 2): "))

if option == 1:
    # Prompt the user for the equation and method
    equation = input("Enter the equation: ")
    method = int(input("Choose a method (1. Bisection, 2. Newton-Raphson, 3. Secant): "))

    # Prompt the user for initial guesses and convergence criteria
    a = float(input("Enter the lower bound of the interval: "))
    b = float(input("Enter the upper bound of the interval: "))
    epsilon = float(input("Enter the desired accuracy (epsilon): "))
    max_iterations = int(input("Enter the maximum number of iterations: "))

    # Define the function based on the equation entered by the user
    def func(x):
        return eval(equation)

    # Define the derivative function based on the equation entered by the user
    def derivative(x):
        return eval(equation.replace("x", str(x), 1))

    # Find the root using the selected method
    if method == 1:
        root, elapsed_time = bisection_method(func, a, b, epsilon, max_iterations)
    elif method == 2:
        initial_guess = float(input("Enter the initial guess: "))
        root, elapsed_time = newton_raphson_method(func, derivative, initial_guess, epsilon, max_iterations)
    elif method == 3:
        initial_guess_1 = float(input("Enter the first initial guess: "))
        initial_guess_2 = float(input("Enter the second initial guess: "))
        root, elapsed_time = secant_method(func, initial_guess_1, initial_guess_2, epsilon, max_iterations)
    else:
        print("Invalid method choice.")

    # Display the result
    if root is not None:
        print("The root is:", root)
        print("Elapsed time:", elapsed_time, "seconds")

elif option == 2:
    # Prompt the user for the equation and method
    equation = input("Enter the equation for dy/dx: ")
    method = int(input("Choose a method (1. Taylor series, 2. Picard, 3. Euler): "))

    # Prompt the user for initial values and step size
    x0 = float(input("Enter the initial value of x: "))
    y0 = float(input("Enter the initial value of y: "))
    x = float(input("Enter the value of x at which to estimate y: "))
    n = int(input("Enter the number of iterations (for Taylor series or Euler's method): "))

    # Define the function based on the equation entered by the user
    def func(x, y):
        return eval(equation)

    # Solve the differential equation using the selected method
    if method == 1:
        y = taylor_series_method(func, derivative, x0, y0, x, n)
    elif method == 2:
        y = picard_method(func, x0, y0, x, n)
    elif method == 3:
        y = euler_method(func, x0, y0, x, n)
    else:
        print("Invalid method choice.")

    # Display the result
    print("The estimated value of y at x =", x, "is:", y)

else:
    print("Invalid option choice.")





# Example equation: x^2 - 4
# Example derivative: 2x

# Example differential equation: dy/dx = x^2 - 4
# Example solution: y = (1/3)x^3 - 4x + C, where C is the constant of integration

# Testing the root finding functionality

equation = "x**2 - 4"
method = 1  # Bisection method

a = -10
b = 10
epsilon = 0.001
max_iterations = 100

print("Root Finding:")
print("Equation:", equation)
print("Method: Bisection")
print("Interval: [{}, {}]".format(a, b))
print("Desired Accuracy (epsilon):", epsilon)
print("Maximum Iterations:", max_iterations)

def func(x):
    return eval(equation)

def derivative(x):
    return eval(equation.replace("x", str(x), 1))

root, elapsed_time = bisection_method(func, a, b, epsilon, max_iterations)
print("Root found:", root)
print("Elapsed time:", elapsed_time, "seconds")

print("---------------------------------------")

# Testing the ordinary differential equation solving functionality

equation = "x**2 - 4"
method = 2  # Picard's method

x0 = 0
y0 = 0
x = 2
n = 100

print("Ordinary Differential Equation Solving:")
print("Equation: dy/dx =", equation)
print("Method: Picard's Method")
print("Initial value of x:", x0)
print("Initial value of y:", y0)
print("Value of x at which to estimate y:", x)
print("Number of iterations:", n)

def func(x, y):
    return eval(equation)

y = picard_method(func, x0, y0, x, n)
print("Estimated value of y at x =", x, ":", y)

print("---------------------------------------")

# Testing an invalid option choice

option = 3

print("Invalid Option Choice:")
print("Option:", option)

print("---------------------------------------")
