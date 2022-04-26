import numpy as np

def rk4_multidimensional(func: str,
                         t_0: float,
                         pont: float,
                         x_0: np.array,
                         lepeskoz: float):

    x = x_0
    t = t_0
    t_end = pont
    h = lepeskoz
    while t < t_end:
        k_0 = globals()[func](t, x)
        x_1 = x + h / 2 * k_0
        k_1 = globals()[func](t + h / 2, x_1)
        x_2 = x + h/2 * k_1
        k_2 = globals()[func](t +h/2, x_2)
        x_3 = x + h * k_2
        k_3 = globals()[func](t + h, x_3)
        x = x + h/6 * (k_0 + 2*k_1 + 2*k_2 + k_3)
        t = t + h

    return x

def reduced_to_ode():
    A = np.array([[0,1],[-2,3]])
    x = np.array([[2],[-3]])
    pass