
def euler_method(t: float,
                 f: str,
                 t_0: float,
                 kezdeti_ertek: float,
                 lepeskoz: int):
    """
    :param t: Adott pont, ahol kiertekeljuk a differencial egyenletet
    :param f: Fuggveny neve, amiben implementaltuk az egyeneletet
    :param t_0: Kezdeti ertek ido pillanata
    :param kezdeti_ertek: Maga a kezdeti ertek
    :param lepeskoz: Iteracios lepesek szama
    :return: A differencial egyenlet Euler metodus szerinti kozelitese
    """

    t_i = t_0
    x = kezdeti_ertek
    h = ((t - t_0) / lepeskoz)
    for i in range(lepeskoz):
        t_i = t_i + h
        x = x + h * globals()[f](t_i, x)

    return x
