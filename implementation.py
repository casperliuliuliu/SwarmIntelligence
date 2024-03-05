from brute_force import brute_force
from data_generation import get_test_data_of_hill
from data_generation import plot_x_y

def test_algorithm(task, algorithm):
    features, labels = get_test_data_of_hill()
    if algorithm == "brute_force":
        ss = brute_force(features, labels, True)
        print(ss)

if __name__ == "__main__":
    test_algorithm('maxima', 'brute_force')