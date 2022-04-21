import numpy as np


def increase_on_index(index_of_element: int, list_of_parameters: list) -> list:
    h = 0.00001
    list_to_modify = list_of_parameters.copy()
    list_to_modify[index_of_element] += h
    return list_to_modify


def derivate_on_each_variable(func: str, parameter_list: np.array) -> np.array:
    h = 0.00001

    for index in range(len(parameter_list)):
        point_array = increase_on_index(index, parameter_list)
        value = (globals()[func](point_array) - globals()[func](parameter_list)) / h
        if index == 0:

            output = np.array([value])
        else:
            output = np.append(output, value)
    return output


def create_numerical_jacobi(function_list: list, parameter_list: np.array):
    jacobi = np.empty([len(parameter_list), len(parameter_list)], dtype=float)
    index = 0
    for function in function_list:
        jacobi[index] = derivate_on_each_variable(str(function), parameter_list)
        index += 1
    return jacobi
