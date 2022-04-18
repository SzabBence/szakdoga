import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 1)
y = np.power(x, 2)
y_3 = np.power(x, 3)

plt.plot(x, y, c="r", label="x^2")
plt.plot(x, y_3, c="b", label="x^3")
plt.xlabel("x tengely felirata")
plt.ylabel("y tengely felirata")
plt.hlines(
    y=200,
    xmin=0,
    xmax=10,
    color="orange",
    linestyle="--",
    label="vízszintes szaggatott vonal",
)
plt.vlines(
    x=5, ymin=0, ymax=1000, color="black", linestyle="dashdot", label="függőleges vonal"
)
plt.legend()
plt.show()
