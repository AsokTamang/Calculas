from sympy import *

print(sqrt(18))

x,y = symbols('x y')
expression = 3 * x**2 + y
print(expression)

additional_expression = x * expression
print(additional_expression)

expanded = expand(additional_expression)  #we are expanding the expression
print(expanded)

factorised = factor(expanded)
print(factorised)
