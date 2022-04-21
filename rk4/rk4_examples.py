def dydx(input_list: list):

    return (input_list[0] - input_list[1]) / 2


def kamatlab(input_list: list):
    r = 0.1
    x = input_list[1]
    return r * x


def konstans(x: list):
    """
    Az 1 indexu elemet kerjuk ki, mert ebben a peldaban igy mukodik helyesen a fuggveny
    """
    return 5 * x[1] - 3


def harmadfoku(x: list):

    return np.power(x[1], 3) / 3


def bonyolultabb(x: list):
    t = x[0]
    x_t = x[1]

    return 1 / (x_t * (9 + 4 * t**2))


# A ket feladat numerikus megoldasa:
if __name__ == "__main__":
    t_0 = 0
    x_0 = 1
    t = 1
    h = 0.01
    print("A kamatlab feladat numerikus eredmenye: \n")
    print(str(rk4(h, t_0, x_0, t, "kamatlab")))

    t_0 = 0
    x_0 = 1
    t = 1
    h = 0.01
    print("A konstans egyutthatos feladat numerikus eredmenye: \n")
    print(str(rk4(h, t_0, x_0, t, "konstans")))

    t_0 = 0
    x_0 = 3
    t = 0.1
    h = 0.01
    print("A harmadfoku feladat numerikus eredmenye: \n")
    print(str(rk4(h, t_0, x_0, t, "harmadfoku")))

    t_0 = 0
    x_0 = 1
    t = 0.1
    h = 0.01
    print("A bonyolultabb feladat numerikus eredmenye: \n")
    print(str(rk4(h, t_0, x_0, t, "bonyolultabb")))
