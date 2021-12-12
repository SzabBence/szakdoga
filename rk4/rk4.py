def rk4(lepeskoz: float,
        kezdeti_pont: float,
        kezdeti_ertek: float,
        pont: float,
        func: str) -> float:
    """

    :param lepeskoz: h
    :param kezdeti_pont: x_0
    :param kezdeti_ertek: y_0
    :param pont: x
    :param func: fuggveny neve, amivel a problemat megoldjuk
    :return: RK4 kozelitese a feladatnnak
    """
    n = int((pont - kezdeti_pont) / lepeskoz)

    y = kezdeti_ertek
    for i in range(1, n + 1):
        k1 = lepeskoz * globals()[func]([kezdeti_pont, y])
        k2 = lepeskoz * globals()[func]([kezdeti_pont + 0.5 * lepeskoz, y + 0.5 * k1])
        k3 = lepeskoz * globals()[func]([kezdeti_pont + 0.5 * lepeskoz, y + 0.5 * k2])
        k4 = lepeskoz * globals()[func]([kezdeti_pont + lepeskoz, y + k3])
        y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

        kezdeti_pont = kezdeti_pont + lepeskoz

    return y


def dydx(input_list: list):
    """

    :param input_list: fuggveny parameterei
    :return: fuggveny erteke
    """
    return (input_list[0] - input_list[1]) / 2


if __name__ == "__main__":
    x0 = 0
    y = 1
    x = 2
    h = 0.2
    print('A fuggveny erteke az x=' + str(x) + " pontban: " + str(rk4(h, x0, y, x, "dydx")))
