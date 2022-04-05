
def euler_method(t: float,
                 f: str,
                 t_0: float,
                 kezdeti_ertek: float,
                 lepeskoz: int):

    t_i = t_0
    x = kezdeti_ertek
    h = ((t - t_0) / lepeskoz)
    for i in range(lepeskoz):
        t_i = t_i + h
        x = x + h * globals()[f](t_i, x)

    return x


def pelda(t, x_t):

    return 1 / (x_t * (9 + 4 * t**2))


def konstans(t, x):

    return 5 * x - 3
if __name__ == '__main__':
    n = 50
    h = 0.01
    t_0 = 0
    x_0 = 1
    pont = 1
    lepeskoz = 10
    print("Elso pelda:")
    print(euler_method(pont, "pelda", t_0, x_0, n))
    print("*" * 20)
    print("Masodik pelda")
    print(euler_method(pont, "konstans", t_0, x_0, n))