from sympy import *
from sympy.utilities.lambdify import lambdify
import numpy as np
import jax.numpy as jnp
from jax import vmap,grad
print(sqrt(18))

def f(x):  #function returning normal line
    return x**2

x,y = symbols('x y')
expression = 3 * x**2 + y
print(expression)

additional_expression = x * expression
print(additional_expression)

expanded = expand(additional_expression)  #we are expanding the expression
print(expanded)

factorised = factor(expanded)
print(factorised)

expression.evalf(subs={x:1,y:2})  #here we are substituting the value of x and y with 1 and 2 respectively.
a_array = np.array([1,2,3])

f_calculation = x ** 2
f_new_calculations =lambdify(x, f_calculation,'numpy')  #taking x input for f_calculation using module numpy
print(f_new_calculations(a_array))


b=np.array([1,2,3])
dfdx_symb =lambdify(x,diff(f(x),x),'numpy')(b)   #calculating the derivative using symbolic method

dfdx_numeric = np.gradient(f(b),b)  #using numeric method

dfdx_automatic = vmap(grad(f))(jnp.array(b.astype('float32')))  #this is way faster and effective for larger size arrays cause it uses chain rule


