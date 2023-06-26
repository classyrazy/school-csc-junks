'''
Name: Adewale Abdulrazaq Olabiyi
Matric number: 190806014
Department: Mathematics
'''
import random
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


def main(lst):
    if len(lst) == 6:
        return f"The approximate root of {lst[0]}x^{lst[3]} + {lst[1]}x + {lst[2]} = 0 is {random.choice([secant_method(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5]), bisection_method(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5])])} "
    elif len(lst) == 5:
        return f"The approximate root of {lst[0]}x^{lst[3]} + {lst[1]}x + {lst[2]} = 0 is {newton_raphson_method(lst[0],lst[1],lst[2],lst[3],lst[4])}"
    else:
        return "The number of arguments must be a length of 5 to 6 coefficeints"
         
print(main([1, 0, -3, 2, 1, 2]))
