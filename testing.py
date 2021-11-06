import numpy as np

def squared(x: np.array,params: np.array) -> float:
    a = params[0]
    b = params[1]
    c = params[2]
    return np.power(a * x,2) + b * x + c

def trapez_method(x: np.array, func: str, func_params = None) -> float:
    y = globals()[func](x, func_params)
    s = 0
    for i in range(len(x) - 1):
        s = 0.5 * (y[i] + y[i + 1]) * (x[i + 1] - x [i])
    return s

#Inputs = np.array([1,2])
#values = trapez_method(Inputs,"squared",[1,2,0])

intervals_to_integrate = np.asarray([[1,1.33], [1.33,1.66],[1.66,2]])
integrate_sum = 0
squared_params = np.array([1,2,0])
for interval_to_integrate in intervals_to_integrate:
    integrate_sum = integrate_sum + trapez_method(interval_to_integrate,"squared",squared_params)
    print(integrate_sum)