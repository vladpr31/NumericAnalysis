import math
import scipy.special
import sympy as sy
import sympy as sp
from sympy import sympify


# function for Gauss-Legendre rule
def gauss(f, n, b, a):
    G = 0
    nodes, weights = scipy.special.p_roots(n)
    for i in range(n):
        G += 0.5 * (b - a) * (weights[i] * f(0.5 * (b - a) * nodes[i] + 0.5 * (b + a)))
    return G


x, y = sy.symbols("x,y")

# inputs for the user
flag = int(input("Press 1 for normal integral ,Press 2 for double integral: "))
if flag == 1:
    points = int(input("input the number of points you want to work with: "))
    up = float(input("input the upper bound: "))
    down = float(input("input the lower bound: "))
    my_f = input("input your function: ")
    new = sp.lambdify(x, my_f)
    print("solution: ", gauss(new, points, up, down))
else:
    points = int(input("input the number of points you want to work with: "))

    print("\n--for the nested integral--")
    up = float(input("input the upper bound: "))
    down = float(input("input the lower bound: "))

    print("\n--for the outside integral--")
    up1 = float(input("input the upper bound: "))
    down1 = float(input("input the lower bound: "))

    my_f = sympify(input("input your function: "))

    new = sp.lambdify(x, my_f)
    new1 = sp.lambdify(y, gauss(new, points, up, down))
    print("solution: ", gauss(new1, points, up1, down1))
