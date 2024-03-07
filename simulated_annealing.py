from visualization_function import process_visualization
from evaluation import eval
import random
import math
def simulated_annealing(datas, labels, visualization=False):
    """
    Pseudo:
    initialize temperate tt
    initialize solution ss
    evaluation function eval()
    f1 = eval(s)
    while #loop over all s
        v = fetch next()
        f2 = eval(v)
        if r < Pa
            s = v
            f1 = f2
        update temperature
    return s
    """

    def temperature(time):
        return 100.0 / (1 + time)
    
    def acceptance_probability(old_value, new_value, temperature):
        if new_value > old_value:
            return 1.0
        else:
            return math.exp( - 1 / temperature)
    
    # Initialize temperature and solution
    times = 1
    lower_bound = -1
    upper_bound = len(datas)
    ss, index = initial_solution(datas)
    best_ss, best_value = ss, index
    f1 = eval(ss, labels)
    last_vv, last_index = ss, index
    while times <= 200:
        vv, index = SA_neighbor_selection(datas, index, lower_bound, upper_bound)
        f2 = eval(vv, labels)
        r = random.random()
        prob = acceptance_probability(f1, f2, temperature(times))
        # print(prob, r)
        if f2 > best_value:
            best_ss, best_value = vv, f2

        if r < prob:
            # print('change')
            ss = vv
            f1 = f2
        else:
            vv, index = last_vv, last_index
            f2 = eval(vv, labels)

        if visualization:
            plt = process_visualization(datas, labels, best_ss, best_value, vv, f2, times, temperature(times))
        times += 1
        last_vv, last_index = vv, index

    print('[Simulated Annealing Done]')
    # plt.show()
    return best_value

def initial_solution(datas):
    random_index = random.randint(0, len(datas)-1)
    random_index = 95
    return datas[random_index], random_index


def SA_neighbor_selection(datas, index, lower_bound, upper_bound):
    r = random.random()
    if r > 0.4:
        index +=1
    else:
        index -=1

    if index >= upper_bound:
        index -=2
    if index <= lower_bound:
        index +=2

    return datas[index], index
    



    



