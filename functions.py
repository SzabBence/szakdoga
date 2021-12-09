import numpy as np

def trapez_method(x: np.array,
                  func: str,
                  func_params: np.array) -> float:
    y = globals()[func](x, func_params)
    s = 0
    for i in range(len(x) - 1):
        s = 0.5 * (y[i] + y[i + 1]) * (x[i + 1] - x[i])
    return s

def squared(x: np.array,
            params: np.array) -> float:
    a = params[0]
    b = params[1]
    c = params[2]
    return np.power(a * x, 2) + b * x + c
