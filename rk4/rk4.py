# Python program to implement Runge Kutta method
# A sample differential equation "dy / dx = (x - y)/2"


def rk4_dydx(lepeskoz,
             kezdeti_pont,
             kezdeti_ertek,
             pont) -> float:
    """

    :param lepeskoz: h
    :param kezdeti_pont: x_0
    :param kezdeti_ertek: y_0
    :param pont: x
    :return: RK4 kozelitese a feladatnnak
    """
    n = int((pont - kezdeti_pont) / lepeskoz)

    y = kezdeti_ertek
    for i in range(1, n + 1):

        k1 = lepeskoz * dydx([kezdeti_pont, y])
        k2 = lepeskoz * dydx([kezdeti_pont + 0.5 * lepeskoz, y + 0.5 * k1])
        k3 = lepeskoz * dydx([kezdeti_pont + 0.5 * lepeskoz, y + 0.5 * k2])
        k4 = lepeskoz * dydx([kezdeti_pont + lepeskoz, y + k3])

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
    print('A fuggveny erteke az x=' + str(x) + " pontban: " + str(rk4_dydx(h, x0, y, x)))
