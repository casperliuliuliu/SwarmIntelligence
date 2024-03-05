import numpy as np
import matplotlib.pyplot as plt

def generating_data(x_values, noise=0):
    y_values = []
    for x in x_values:
        y = test_hill_formula(x)
        y_values.append(y)
    return y_values

def test_hill_formula(x):
    return -(x-2)*(x)*(x+5)*(x-5)*(x+6)*(x-8)+3000


def plot_x_y(x_values, y_values, title='Function Plot', xlabel='x', ylabel='y'):
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.show()

def get_test_data_of_hill():
    x_values = [ii/10 for ii in range(-60, 80, 1)]
    y_values = generating_data(x_values)
    return np.array(x_values), np.array(y_values)

if __name__ == "__main__":
    x_values = [ii/10 for ii in range(-60, 80, 1)]
    y_values = generating_data(x_values)
    plot_x_y(x_values,y_values)

        