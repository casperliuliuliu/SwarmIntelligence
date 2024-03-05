import matplotlib.pyplot as plt

def plot_xy_pairs_with_pause(xy_pairs):
    """
    Plot 5 pairs of x and y values with a time lapse of 1 second between each.

    Parameters:
    - xy_pairs: A list of tuples, where each tuple is a pair of x and y values.
    """
    plt.figure(figsize=(10, 6))
    # plt.ion()  # Turn on interactive plotting
    
    for x, y in xy_pairs:
        plt.scatter(x, y, label=f'Point ({x}, {y})')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.xlim(0,20)
        plt.ylim(0,20)
        plt.title('Interactive Plotting of x and y Pairs')
        plt.legend()
        plt.grid(True)
        plt.draw()
        plt.pause(0.3)  # Pause for 1 second
        plt.clf()  # Clear the plot for the next iteration
    
    plt.show()

# Example usage with 5 pairs of x and y
xy_pairs = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10)]

plot_xy_pairs_with_pause(xy_pairs)
