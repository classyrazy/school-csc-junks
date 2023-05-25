

# Bisection method
import math


def bisection_method(f, a, b, tol=1e-6, max_iter=1000):
    """
    Solve the equation f(x) = 0 using the bisection method.

    Args:
        f (function): The function whose roots are to be found.
        a (float): The left end of the interval.
        b (float): The right end of the interval.
        tol (float): The tolerance for the solution.
        max_iter (int): The maximum number of iterations allowed.

    Returns:
        float: The approximate root of f(x) = 0.
    """
    # Check that f(a) and f(b) have opposite signs
    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    # Initialize variables
    c = (a + b) / 2
    iter_count = 0

    # Iterate until convergence or max iterations is reached
    while abs(f(c)) > tol and iter_count < max_iter:
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
        iter_count += 1

    # Check if the maximum number of iterations was reached
    if iter_count == max_iter:
        print("Maximum number of iterations reached.")

    return c


# Define the function to be solved

def f(x):
    return x ** 3 - math.cos(x)


# Solve the equation using the bisection method
a = 0
b = 1
root = bisection_method(f, a, b)

# Print the root
print("The bisection root is:", root)

# The secant method


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

    # Iterate until the desired accuracy is achieved or the maximum iterations are reached
    while abs(func(x_curr)) > epsilon and iterations < max_iterations:
        # Calculate the next approximation using the secant method formula
        x_next = x_curr - (func(x_curr) * (x_curr - x_prev)
                           ) / (func(x_curr) - func(x_prev))

        # Update the current and previous approximations
        x_prev = x_curr
        x_curr = x_next

        # Increment the iteration counter
        iterations += 1

    # Check if the method converged within the maximum iterations
    if iterations == max_iterations:
        print("Maximum iterations reached. The method did not converge.")

    # Return the estimated root
    return x_curr


# Define the function to be solved
def fBSecant(x):
    return x ** 3 - math.cos(x)


# Solve the equation using the secant method
x0 = 0
x1 = 1
secant_root = secant_method(fBSecant, x0, x1, 1e-6, 1000)

# Print the root
print("The secant root is:", secant_root)

# Newton raphson method


def newton_raphson(f, f_prime, initial_guess, epsilon=1e-6, max_iterations=100):
    x = initial_guess
    iteration = 0

    while abs(f(x)) > epsilon and iteration < max_iterations:
        x = x - f(x) / f_prime(x)
        iteration += 1

    if iteration == max_iterations:
        print("Maximum iterations reached. No convergence.")

    return x

# Define the function to be solved
def fBNewton(x):
    return x ** 3 - math.cos(x)

# Define the derivative of the function
def fBPrimeNewton(x):
    return 3 * x ** 2 + math.sin(x)

# Solve the equation using the Newton-Raphson method
initial_guess = 1.0
newton_raphson_root = newton_raphson(fBNewton, fBPrimeNewton, initial_guess)

# Print the root
print("The Newton-Raphson root is:", newton_raphson_root)


