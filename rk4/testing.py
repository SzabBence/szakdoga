import numpy as np
def func_wrapper(x,t):
    x1 = x[0]
    x2 = x[1]
    return np.array([[x2],[-2 * x1 + 3* x2 + t]])

x1 = 2
x2 = - 3
x = np.array([[x1], [x2]])
h=0.01
pont = 1
t = 0
t_end = pont
arraynum = np.array([[2], -3])
while t < t_end:
    k_0 = func_wrapper(x,t)
    x_1 = x + h/2 * k_0
    k_1 = func_wrapper(x,t)
    x_2 = x + h/2 * k_1
    k_2 = func_wrapper(x,t)
    x_3 = x + k_2
    k_3 = func_wrapper(x,t)
    x = x + h/6 * (k_0 + 2 * k_1 + 2 * k_2 + k_3)
    print(x)
    t = t + h



