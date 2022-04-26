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
def f1(t: float,x: np.array) -> float:
    x_1 = x[0]
    x_2 = x[1]
    return x_1

def f2(t: float,x: np.array) -> float:
    x_1 = x[0]
    x_2 = x[1]

    return -2 * x_1 + 3 * x_2 + t

def func_wrapper(func_list : list,
                 t:float,
                 X: np.array):
    result = np.array([])
    for func in func_list:
        if result.size == 0:
            result = globals()[func](t, X)
        else:
            result.append(result, globals()[func](t, X), axis=0)

    return result
if __name__ == "__main__":
    x_0 = np.array([[2],[-3]])
    t_0 = 0
    pont = 1
    h = 0.001
    func_list = ["f1", "f2"]
    print(rk4_multidimensional("reduced_to_ode",t_0,pont,x_0,h))