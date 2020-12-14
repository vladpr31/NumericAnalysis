import sympy as sp
from sympy import ln


def Bisection_method(p, a, b, e=0.000001):
    p_a = a
    p_b = b
    while (p_b - p_a) > e:
        p_m = (p_a + p_b) / 2
        if p(p_m) == 0:
            return p_m
        else:
            if p(p_a) * p(p_m) < 0:
                p_a = p_a
                p_b = p_m
            elif p(p_b) * p(p_m) < 0:
                p_a = p_m
                p_b = p_b
    return (p_a + p_b) / 2
def To_Bisection(f, a, b, N):
    x_one = 0
    x_two = 0
    d = (abs(a) + abs(b)) / N
    flag=0
    err=abs(round((ln((0.000001 / (b - a))) / ln(2)) + 1))
    for i in range(1, N + 1):
        if f(a) * (f(a + d)) < 0:
            if f(a) < 0 and f(a + d) > 0:
                x_one = a
                x_two = a + d
                if (round(Origin_Func(Bisection_method(f, x_one, x_two)))) == 0:
                    if round(x_two,1)==0 or round(x_one,1)==0:
                         x_two = a + d +d
                    print(i,"-For Range(", round(x_two,1), ",", round(x_one,1), ") The Point is:", round(Bisection_method(f, x_one, x_two),5))
                    flag=1
                a = a + d
                if a+d ==0:
                    a=a+d+d
            if f(a) > 0 and f(a + d) < 0:
                x_one = a
                x_two = a + d
                if (round(Origin_Func(Bisection_method(f, x_one, x_two)))) == 0:
                    if round(x_two,1)==0 or round(x_one,1)==0:
                         x_two = a + d +d
                    print(i,"-For Range(", round(x_two,1), ",", round(x_one,1), ") The Point is:", round(Bisection_method(f, x_one, x_two),5))
                    flag=1
                a = a + d
                if a+d ==0:
                    a=a+d+d
            else:
                a = a + d
                if a+d ==0:
                    a=a+d+d
        else:
            a = a + d
            if a + d == 0:
                a = a + d + d
        if i == err and flag == 0 and f(1) == Origin_Func(1):
            print('Function Reached Error limit, this function cannot use Bisection Method.')
            break
def To_derivative(f):
    my_f = f
    d1 = (sp.diff(my_f))
    return d1
def Origin_Func(x):
    return x**4+x**3-3*x**2 #Origin Function

x = sp.symbols('x')
# Input Section
x0 = int(input('First Range: '))
x1 = int(input('Second Range: '))
section = int(input('Sections for division: '))

To_Bisection(lambda x:x**4+x**3-3*x**2, x0, x1, section)
To_Bisection(To_derivative(sp.Poly(x**4+x**3-3*x**2)), x0, x1, section)