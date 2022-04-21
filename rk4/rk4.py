def rk4(
    lepeskoz: float, kezdeti_pont: float, kezdeti_ertek: float, pont: float, func: str
) -> float:
    """
    Ha x(t_0) = x_0 felirasban nezzuk, akkor és x(t) = ...
    :param lepeskoz: h
    :param kezdeti_pont: t_0
    :param kezdeti_ertek: x_0
    :param pont: t
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
