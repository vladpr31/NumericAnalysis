import sympy as sp
from sympy import ln
import math

def Newton_Raphson(p,start_point,end_point,e=0.000001):
    count=1
    Flag=True
    f=sp.lambdify(x,p)
    f_tag=sp.lambdify(x,To_derivative(p))
    if round(f(start_point),6)>0 and round(f(end_point),6)<0 or round(f(start_point),6)<0 and round(f(end_point),6)>0:
     start_point=(start_point+end_point)/2
     while Flag:
        if f_tag(start_point)==0:
            print("Cant Divide by Zero.")
            break
        else:
         x1= start_point - ((f(start_point))/(f_tag(start_point)))
         start_point=x1
         print("Iteration num:",count,"      x1=",round(x1,6),'      Func(x):',round(f(x1),6),'        xr=',round(start_point,6))
         count += 1
         Flag=f(x1)>=e
     print("Root is:",round(x1,6),' at Iteration:',count-1)
    else:
        print("Error Occoured, The range you've inputed are not good.")
def To_derivative(f):
    my_f = f
    d1 = sp.diff(my_f)
    return d1
def secant_method(f,xi, xi1, e=0.000001):
    print('\n\nSECANT METHOD IMPLEMENTATION')
    step = 1
    condition = True
    if f(xi) > 0 and f(xi1) > 0 or f(xi1) < 0 and f(xi) < 0:
        print('we didnt find solution in this range try again')
        return False

    print('Iteration %d, xi=%0.6f, xi+1 = %0.6f ,f(xi) = %0.6f' % (step,xi,xi1, f(xi)))
    step = step +1
    while condition:
        x2 = xi - (xi1 - xi) * f(xi) / (f(xi1) - f(xi))
        xi = xi1
        xi1 = x2
        print('Iteration %d, xi=%0.6f, xi+1 = %0.6f ,f(xi) = %0.6f' % (step,xi,xi1, f(xi)))
        step = step + 1


        condition = abs(xi-xi1) > e or round(f(xi))!=0
    print('\n Required root is: %0.6f' % xi1)


# Input Section
p = lambda x: x ** 3 - math.cos(x)
print("##### Secant Method #####")
print("Uses the function of p.")
print("########################")
xi = float(input('Enter First Range: ')) # (0,1)
xi1 = float(input('Enter Second Range: ')) # (0,1) for the p example.
secant_method(p,xi, xi1)
print("\n")
print("##### Newton Raphson Method #####")
print("uses the function of func.\n")
print("##################################")
x=sp.symbols('x')
func=x**3-x-1
Newton_Raphson(func,1,10)


