def successive_approx(y0: float,
                       n: int,
                       func: str,
                       params: dict):
    """

    :param y0: kezdeti ertek
    :param n: hanyadik lepesig megyunk el
    :param func: fuggveny, amivel definialjuk a problemat
    :param params: func parameterei
    :return: fokozatos kozelitesek modszerevel kapott megoldas

    Fontos: az 'integral' fuggveny egyelore nem definialt, de feltesszuk, hogy megmondjuk a func parameterben, hogy
    mi a fuggveny, amit integralni szeretnenk, a params inputban pedig a fuggveny minden valtozojat
    """
    if n==1:
        return y0 + integral(func, params)
    elif n < 1:
        return "Nem lehet n<1"
    else:
        return y0 + integral("successive_approx", [y0, n - 1])

def integral(func: str,
             params: list):

    return None