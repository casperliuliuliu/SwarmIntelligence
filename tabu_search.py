from visualization_function import TS_process_visualization
from evaluation import eval
import random

def tabu_search(datas, labels, visualization=False, tabu_size=20, max_iterations=100):

    ss, ss_index = initial_solution(datas)
    f1 = eval(ss, labels)

    best_solution = ss
    best_solution_score = f1

    tabu_list = []  # Initialize the tabu list

    iteration = 0
    while iteration < max_iterations:
        neighbors = TS_get_neighbors(datas, ss_index, tabu_list)
        best_neighbor, best_neighbor_index = None, -1
        best_neighbor_score = -float('inf')  # Assume we are maximizing

        for neighbor, index in neighbors:
            if index not in tabu_list:
                f2 = eval(neighbor, labels)
                if f2 > best_neighbor_score:
                    best_neighbor = neighbor
                    best_neighbor_score = f2
                    best_neighbor_index = index

        if best_neighbor is None:
            break  # No improvement possible, exit the loop

        # Update the current solution
        ss = best_neighbor
        ss_index = best_neighbor_index
        f1 = best_neighbor_score

        # Update the best solution found so far
        if f1 > best_solution_score:
            best_solution = ss
            best_solution_score = f1

        # Update the tabu list
        tabu_list.append(ss_index)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
        print(tabu_list)

        iteration += 1

        if visualization:
            plt = TS_process_visualization(datas, labels, best_solution, best_solution_score, ss, f1, tabu_list, datas, labels)

    if visualization:
        print('[Tabu Search Done]')
        plt.show()

    return best_solution

def initial_solution(datas):
    random_index = random.randint(0, len(datas)-1)
    random_index = 45
    return datas[random_index], random_index

def TS_get_neighbors(datas, current_index, tabu_list, perturbation_range=20, num_neighbors=5):
    neighbors = []
    len_solution = len(datas)

    for _ in range(num_neighbors):

        element_index = current_index

        perturbation = int(random.uniform(-perturbation_range, perturbation_range))

        element_index += perturbation
        
        # Ensure the neighbor is not in the tabu list and not the same as the current solution
        # This check is simplistic and might need refinement based on how solutions are compared or hashed
        if element_index not in tabu_list and element_index != current_index and 0 <= element_index and element_index < len_solution:
            neighbors.append((datas[element_index], element_index))
    
    return neighbors

