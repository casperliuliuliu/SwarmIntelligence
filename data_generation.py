import numpy as np
import matplotlib.pyplot as plt

def generating_data(x_list, noise=0):
    y_list = []
    for x in x_list:
        y = hill_function(x)
        y_list.append(y)
    return y_list

def hill_function(x):
    return -(x-2)*(x)*(x+5)*(x-5)*(x+8)*(x-8)+3000


def plot_x_y(x_values, y_values, title='Function Plot', xlabel='x', ylabel='y'):
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.show()

def data_combine(x_list, y_list):
    return np.array([x_list, y_list])

def get_test_data_of_hill():
    x_list = [ii/10 for ii in range(-80, 80, 1)]
    y_list = generating_data(x_list)
    return data_combine(x_list,y_list)

if __name__ == "__main__":
    x_list = [ii/10 for ii in range(-80, 80, 1)]
    y_list = generating_data(x_list)
    plot_x_y(x_list,y_list)
    print(data_combine(x_list,y_list))

        