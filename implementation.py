from brute_force import brute_force
from hill_climbing import hill_climbing
from simulated_annealing import simulated_annealing
from tabu_search import tabu_search
from data_generation import get_test_data_of_hill
from data_generation import plot_x_y

def test_algorithm(task, algorithm):
    features, labels = get_test_data_of_hill()
    if algorithm == "brute_force":
        ss = brute_force(features, labels, True)
    elif algorithm == "hill_climbing":
        ss = hill_climbing(features, labels, True)
    elif algorithm == "simulated_annealing":
        ss = simulated_annealing(features, labels, True)
    elif algorithm == "tabu_search":
        ss = tabu_search(features, labels, True)
    print(ss)


if __name__ == "__main__":
    test_algorithm('maxima', 'tabu_search')