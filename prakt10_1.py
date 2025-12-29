import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 200)
y = 5 * np.sin(x) * (np.cos(x**2 + 1/x))**2

plt.plot(x, y, color="blue", linewidth=3, label="Y(x)")

plt.title("Графік функції Y(x)", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("Y(x)", fontsize=12)
plt.legend()
plt.grid(True)

plt.show()