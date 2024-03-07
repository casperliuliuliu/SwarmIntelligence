from visualization_function import process_visualization
from evaluation import eval
import random

def hill_climbing(datas, labels, visualization=False):
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
    lower_bound = -1
    upper_bound = len(datas)

    ss, index = initial_solution(datas)

    f1 = eval(ss, labels)

    while index != -1:

        vv, index = HC_neighbor_selection(datas, labels, index, lower_bound, upper_bound, f1)

        if index == -1:
            break

        f2 = eval(vv, labels)

        if f2 > f1:
            ss = vv
            f1 = f2
            
        if visualization:
            plt = process_visualization(datas, labels, ss, f1, vv, f2)

    print('[Hill Climbing Done]')
    plt.show()
    return ss

def initial_solution(datas):
    random_index = random.randint(0, len(datas)-1)
    return datas[random_index], random_index


def HC_neighbor_selection(datas, labels, index, lower_bound, upper_bound, f1):
    
    if index+1 < upper_bound:
        vv = datas[index+1]
        f2 = eval(vv, labels)

        if f2 > f1:
            return datas[index+1], index+1
    
    if index-1 > lower_bound:
        vv = datas[index-1]
        f2 = eval(vv, labels)

        if f2 > f1:
            return datas[index-1], index-1
    
    return None, -1




    



