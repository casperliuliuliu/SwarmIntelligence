import matplotlib.pyplot as plt
def process_visualization(x_values, y_values, ss, f1, vv, f2):
    plt.plot(x_values, y_values)
    plt.scatter(vv, f2, label=f'current solution ({vv}, {f2:.2f})', color='orange')
    plt.scatter(ss, f1, label=f'optimal solution ({ss}, {f1:.2f})', color='violet')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Searching for maximum')
    plt.legend()
    plt.grid(True)
    plt.draw()
    plt.pause(0.1)  # Pause for 0.1 second
    plt.clf()  # Clear the plot for the next iteration
    return plt