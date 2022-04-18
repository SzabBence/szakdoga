import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 100
plt.rcParams["legend.loc"] = "center left"
def rk4(lepeskoz: float,
        kezdeti_pont: float,
        kezdeti_ertek: float,
        pont: float,
        func: str) -> list:
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
    list_output = []
    list_output.append(y)
    for i in range(1, n + 1):
        k1 = lepeskoz * globals()[func]([kezdeti_pont, y])
        k2 = lepeskoz * globals()[func]([kezdeti_pont + 0.5 * lepeskoz, y + 0.5 * k1])
        k3 = lepeskoz * globals()[func]([kezdeti_pont + 0.5 * lepeskoz, y + 0.5 * k2])
        k4 = lepeskoz * globals()[func]([kezdeti_pont + lepeskoz, y + k3])
        y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        list_output.append(y)
        kezdeti_pont = kezdeti_pont + lepeskoz

    return [list_output, n]
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
    output = []
    output.append(x)
    for i in range(lepeskoz):
        t_i = t_i + h
        x = x + h * globals()[f](t_i, x)
        output.append(x)
    return [output, lepeskoz]


def kamatlab(input_list: list):
    r = 0.1
    x = input_list[1]
    return r*x


def kamatlab_euler(t, x):
    r = 0.1
    return r*x
if __name__ == '__main__':
    t_0 = 0
    x_0 = 1
    t = 1
    h = 0.01
    megoldasi_ertek = 1.1051709180756475
    output = rk4(h,t_0,x_0,t,"kamatlab")
    euler_lepes = 100
    plt.plot(range(output[1]), output[0][:-1], c="red", label="rk4",linewidth=5)
    output = euler_method(t,"kamatlab_euler",t_0,x_0,euler_lepes)
    plt.plot(range(output[1]), output[0][:-1], c="green", label="euler")
    plt.hlines(y=megoldasi_ertek, xmin=-1, xmax=euler_lepes, color='b', linestyle='--', label = "analitikus eredmény")
    plt.xlabel("Iterácios lépések")
    plt.ylabel("Numerikus közelítések értékei")
    plt.legend()
    plt.show()