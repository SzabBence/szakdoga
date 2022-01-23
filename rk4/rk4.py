def rk4(lepeskoz: float,
        kezdeti_pont: float,
        kezdeti_ertek: float,
        pont: float,
        func: str) -> float:
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


def dydx(input_list: list):
    """

    :param input_list: fuggveny parameterei
    :return: fuggveny erteke
    """
    return (input_list[0] - input_list[1]) / 2

def kamatlab(input_list: list):
    r = 0.1
    x = input_list[1]
    return r*x

def konstans(x: list):
    """
    Az 1 indexu elemet kerjuk ki, mert ebben a peldaban igy mukodik helyesen a fuggveny
    """
    return 5 * x[1] - 3

# A ket feladat numerikus megoldasa:
if __name__ == "__main__":
   t_0 = 0
   x_0 = 1
   t = 1
   h = 0.1
   print("A kamatlab feladat numerikus eredmenye: \n")
   print(str(rk4(h,t_0,x_0,t,"kamatlab")))

   t_0 = 0
   x_0 = 1
   t = 1
   h = 0.01
   print("A konstans egyutthatos feladat numerikus eredmenye: \n")
   print(str(rk4(h,t_0,x_0,t,"konstans")))

