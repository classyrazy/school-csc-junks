import sympy as sp

equation_str = input("Enter the equation (in terms of x): ")
equation = sp.sympify(equation_str)
# f = sp.lambdify(sp.Symbol('x'), equation)
print(equation)