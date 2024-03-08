import matplotlib.pyplot as plt
def process_visualization(x_values, y_values, ss, f1, vv, f2, times=None, temperature=None):
    plt.plot(x_values, y_values)
    plt.scatter(vv, f2, label=f'current solution ({vv}, {f2:.2f})', color='orange')
    plt.scatter(ss, f1, label=f'optimal solution ({ss}, {f1:.2f})', color='violet')
    plt.xlabel('x')
    plt.ylabel('y')
    if temperature:
        plt.title(f'Searching for maximum, times:{times}, temperature:{temperature*100:.2f}')
    else:
        plt.title('Searching for maximum')
    plt.legend()
    plt.grid(True)
    plt.draw()
    plt.pause(0.3)  # Pause for 0.1 second
    plt.clf()  # Clear the plot for the next iteration
    return plt

def TS_process_visualization(x_values, y_values, ss, f1, vv, f2, tabu_list, datas, labels):
    plt.plot(x_values, y_values)
    for tabu_index in tabu_list:
        tabu_x = datas[tabu_index]  # Assuming datas stores x-values
        tabu_y = labels[tabu_index]  # Assuming labels stores corresponding y-values
        plt.scatter(tabu_x, tabu_y, color='red', marker='x')
    plt.scatter(vv, f2, label=f'current solution ({vv}, {f2:.2f})', color='orange')
    plt.scatter(ss, f1, label=f'optimal solution ({ss}, {f1:.2f})', color='blue')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Searching for maximum')
    plt.legend()
    plt.grid(True)
    plt.draw()
    plt.pause(0.3)  # Pause for 0.1 second
    plt.clf()  # Clear the plot for the next iteration
    return plt