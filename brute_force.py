import matplotlib.pyplot as plt

def brute_force(datas, labels, visualization=False):
    """
    Pseudo:
    initial solution s
    evaluation function eval()
    f1 = eval(s)
    while #loop over all s
        v = fetch next()
        f2 = eval(v)
        if f2 > f1
            s = v
            f1 = f2
    return s
    """
    index = 0
    ss = datas[index]

    f1 = eval(ss, labels)

    size = len(datas)
    while index < size:

        vv = datas[index]

        f2 = eval(vv, labels)

        if f2 > f1:
            ss = vv
            f1 = f2
            
        if visualization:
            process_visualization(datas, labels, ss, f1, vv, f2)
        index+=1

    print('[Brute Force Done]')

    return ss

def process_visualization(x_values, y_values, ss, f1, vv, f2):
    plt.plot(x_values, y_values)
    plt.scatter(vv, f2, label=f'solution ({vv}, {f2:.2f})', color='orange')
    plt.scatter(ss, f1, label=f'solution ({ss}, {f1:.2f})', color='violet')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interactive Plotting with Quick Pause')
    plt.legend()
    plt.grid(True)
    plt.draw()
    plt.pause(0.1)  # Pause for 0.1 second
    plt.clf()  # Clear the plot for the next iteration

def eval(ss, labels):
    return labels[int(ss*10+60)]