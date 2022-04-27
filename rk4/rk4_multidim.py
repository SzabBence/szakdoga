import numpy as np

def rk4_multidimensional(func_list: list,
                         t_0: float,
                         pont: float,
                         x_0: np.array,
                         lepeskoz: float):

    x = x_0
    t = t_0
    t_end = pont
    h = lepeskoz

    while t < t_end:
        k_0 = func_wrapper(func_list, t, x)
        x_1 = x + h/2 * k_0
        k_1 = func_wrapper(func_list, t + h / 2, x_1)
        x_2 = x + h/2 * k_1
        k_2 = func_wrapper(func_list, t + h / 2, x_2)
        x_3 = x +  k_2
        k_3 = func_wrapper(func_list, t + h, x_3)
        x = x + h/6 * (k_0 + 2 * k_1 + 2 * k_2 + k_3)
        t = t + h

    return x
def f1(t: float,x: np.array) -> float:
    x_1 = x[0]
    x_2 = x[1]
    return x_1

def f2(t: float,x: np.array) -> float:
    x_1 = x[0]
    x_2 = x[1]

    return -2 * x_1 + 3 * x_2 - t

def f3(t: float,x: np.array):

    return x[1]

def f4(t: float,x: np.array):

    return -x[1] - np.sin(x[0]) + np.sin(t)
def func_wrapper(func_list : list,
                 t:float,
                 X: np.array):
    result = np.empty([len(func_list), 1], dtype=float)
    index = 0
    for func in func_list:
        result[index] = globals()[func](t, X)
        index += 1
    return result
if __name__ == "__main__":
    x_0 = np.array([[2], [-3]])
    t_0 = 0
    pont = 1
    h = 0.0001
    func_list = ["f1", "f2"]
    print(rk4_multidimensional(func_list, t_0, pont, x_0, h))
    print(1)

    # x_0 = np.array([[0], [1]])
    # t_0 = 0
    # h = 0.001
    # pont = 0.2
    # flist = ["f3", "f4"]
    # print(rk4_multidimensional(flist,t_0,pont,x_0,h))