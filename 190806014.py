'''
Name: Adewale Abdulrazaq Olabiyi
Matric number: 190806014
Department: Mathematics
'''

def bisection_method(a, b, c, n, r, s):
    low = min(r, s)
    high = max(r, s)
    
    while abs(high - low) >= 1e-6:
        mid = (low + high) / 2
        equation_value = a * pow(mid, n) + b * mid + c
        
        if equation_value == 0:
            return round(mid, 6)
        
        if equation_value * (a * pow(low, n) + b * low + c) > 0:
            low = mid
        else:
            high = mid
    
    return round((low + high) / 2, 6)


def newton_raphson_method(a, b, c, n, x):
    
    while True:
        equation_value = a * pow(x, n) + b * x + c
        derivative_value = n * a * pow(x, n - 1) + b
        
        if derivative_value == 0:
            return None
        
        x_next = x - equation_value / derivative_value
        
        if abs(x_next - x) < 1e-6:
            return round(x, 6)
        
        x = x_next


def secant_method(a, b, c, n, r, s):
    x0 = r
    x1 = s
    
    while True:
        equation_value0 = a * pow(x0, n) + b * x0 + c
        equation_value1 = a * pow(x1, n) + b * x1 + c
        
        if equation_value1 - equation_value0 == 0:
            return None
        
        x_next = x1 - equation_value1 * (x1 - x0) / (equation_value1 - equation_value0)
        
        if abs(x_next - x1) < 1e-6:
            return round(x_next, 6)
        
        x0 = x1
        x1 = x_next


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

main()
