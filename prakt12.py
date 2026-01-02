import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def cost_function(x):
    """
    Функція витрат
    """
    return x**2 - 6*x + 13

def save_results(x_min, cost_min):
    """
    Збереження результатів у CSV-файл
    """
    data = pd.DataFrame({
        "x_min": [x_min],
        "cost_min": [cost_min]
    })
    data.to_csv("optimization_result.csv", index=False)

def plot_function(x_min, cost_min):
    """
    Побудова графіка функції та точки мінімуму
    """
    x_values = np.linspace(x_min - 5, x_min + 5, 100)
    y_values = cost_function(x_values)

    plt.plot(x_values, y_values)
    plt.scatter(x_min, cost_min)
    plt.xlabel("x")
    plt.ylabel("C(x)")
    plt.title("Оптимізація функції витрат")
    plt.savefig("optimization_plot.png")
    plt.show()

def main():
    try:
        start_value = float(input("Введіть початкове значення x: "))

        print("Виконується пошук мінімуму функції...")
        result = minimize(cost_function, start_value)

        x_min = result.x[0]
        cost_min = result.fun

        print("Результати оптимізації:")
        print(f"Оптимальне значення x = {x_min:.4f}")
        print(f"Мінімальне значення функції = {cost_min:.4f}")

        save_results(x_min, cost_min)
        plot_function(x_min, cost_min)

        print("Результати збережено у файли optimization_result.csv та optimization_plot.png")

    except ValueError:
        print("Помилка: введено некоректне числове значення.")
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except Exception as e:
        print(f"Невідома помилка: {e}")

if __name__ == "__main__":
    main()
