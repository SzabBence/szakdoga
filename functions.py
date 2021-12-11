import numpy as np


def trapez_method(interval: np.array,
                  func: str,
                  func_params: np.array) -> float:
    """
    Ez a fuggveny egy intervallumra elvegzi a trapez terulet szamitast. Figyeljunk arra, hogy celszeru minnel kisebb
    intervallumra alkalmazni a metodust.
    :param interval: Tomb, amely tartalmazza az intervallum kezdo es vegpontjat
    :param func: Fuggveny neve, amelyet integralunk
    :param func_params: Fuggveny parameterei
    :return: Trapez terulete
    """
    y = globals()[func](interval, func_params)

    return (interval[1] - interval[0]) * (y[1] - y[0]) / 2


def squared(x: np.array,
            params: np.array) -> float:
    """
    Ez a fuggveny x minden elemehez hozzarendeli a params altal megadott masodfoku fuggveny erteket
    :param x: Lista, amely minden elemere elvegezzuk a negyzetes fuggvenyt
    :param params: Az a lista, amelybol letrehozzuk a masodfoku fuggvenyt
    :return: np.ndarray tipusu lista a fent leirt muveletek utan
    """
    a = params[0]
    b = params[1]
    c = params[2]
    return np.power(np.multiply(a, x), 2) + np.multiply(b, x) + c


if __name__ == "__main__":
    print(trapez_method(np.array([0, 1]), "squared", [1, 2, 1]))
    print(squared([0], [1, 2, 1]))
    print(squared([0, 1], [1, 2, 1]))
    