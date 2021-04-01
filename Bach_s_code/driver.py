import sys, math
from solver import Solver


def main():
    """"Main driver function"""

    input_list = input("Input list (comma seperated): ")
    input_list = list(map(int, input_list.split(",")))

    n2 = len(input_list)
    n = math.isqrt(len(input_list))

    if n**2 != n2:
        print("Length must be a square.")
        sys.exit()

    if set(input_list) != set(range(n2)):
        print("Input list must contain all numbers from 0 to n^2 - 1.")
        sys.exit()

    try:
        solver = Solver(input_list)
    except ValueError:
        print('No solution exists.')
        sys.exit()

    solution_metrics = solver.dfs()

    print("path_to_goal: ", solution_metrics.path_to_goal)
    print("cost_of_path: ", solution_metrics.cost_of_path())
    print("nodes_expanded: ", solution_metrics.nodes_expanded)
    print("fringe_size: ", solution_metrics.fringe_size())
    print("max_fringe_size: ", solution_metrics.max_fringe_size)
    print("search_depth: ", solution_metrics.search_depth)
    print("max_search_depth: ", solution_metrics.max_search_depth)
    print("running_time: ", solution_metrics.search_time, "ms")


if __name__ == "__main__":
    main()
