from state import State
from metric import Metric
import copy
import math


class Solver:

    """N-Puzzle Solver Class"""
    
    def __init__(self, input_list):
        """Initialise Solver object. Raise ValueError if solution not possible."""
        
        if not self.solvable(input_list):
            raise ValueError('A solution is not possible')

        self.initial_state = copy.deepcopy(self.list_to_grid(input_list)) 

        self.goal_state = self.set_goal_state(input_list)

        self.frontier = []
        self.explored = set()

        self.metrics = Metric(self.frontier)

    def dfs(self):
        """Explore search space using depth-first search"""

        self.metrics.start_timer()

        initial_state = State(self.initial_state)
        self.frontier.append(initial_state)
        
        # while stack is not empty..
        while self.frontier:

            state = self.frontier.pop()

            self.metrics.search_depth = len(state.path_history)
            self.metrics.update_max_depth()

            self.explored.add(state.hash)

            if self.goal_test(state):
                self.metrics.path_to_goal = state.path_history
                self.metrics.stop_timer()
                return self.metrics

            self.expand_nodes(state)

        # dead
        raise ValueError('Shouldn\'t have got to here')

    def expand_nodes(self, starting_state):
        """Take a grid state, add all possible 'next moves' to the frontier"""

        node_order = ['down', 'up', 'right', 'left']

        for node in node_order:   

            # the program is imagining the future!! (maybe change this name...)
            imagined_state = State(starting_state.state)

            # pass path history from previous grid to the next grid
            # using copy to avoid python's reference bindings
            imagined_state.path_history = copy.copy(starting_state.path_history)

            if imagined_state.move(node):  # returns false if move not possible
                
                imagined_state.path_history.append(node)

                if imagined_state.hash not in self.explored:
                    self.frontier.append(imagined_state)
                    self.metrics.update_max_fringe()

            self.metrics.nodes_expanded += 1

    def goal_test(self, state):
        """Compare a given state to the goal state. Return Boolean"""

        if state.state == self.goal_state:
            return True
        else:
            return False

    def list_to_grid(self, tile_list):
        """Take a list of length n^2, return a nxn 2D list"""

        n = math.isqrt(len(tile_list))
        return [tile_list[i:i+n] for i in range(0, len(tile_list), n)]

    def set_goal_state(self, input_list):
        """Construct and return a grid state in the correct order."""

        n = math.isqrt(len(input_list))
        lst = list(range(1, len(input_list))) + [0]
        return [lst[i:i+n] for i in range(0, len(input_list), n)]

    def solvable(self, input_list):
        """Determine if a given input grid is solvable.
        It turns out that a lot of grids are unsolvable.
        http://math.stackexchange.com/questions/293527/how-to-check-if-a-8-puzzle-is-solvable/838818
        http://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html
        
        This implementation assumes blank tile goal position is bottom right.
        """

        # solvability depends on the width...
        width = math.isqrt(len(input_list))

        # ..whether the row that zero is on is odd/even
        temp_state = State(self.list_to_grid(input_list))

        zero_location = temp_state.locate_tile(0, temp_state.state)
        if zero_location[0] % 2 == 0: y_is_even = True
        else: y_is_even = False

        # .. and the number of 'inversions' (not counting '0')

        # strip the blank tile
        input_list = [number for number in input_list if number != 0]

        inversion_count = 0
        list_length = len(input_list)

        for index, value in enumerate(input_list):
            for value_to_compare in input_list[index + 1 : list_length]:
                if value > value_to_compare:
                    inversion_count += 1                    
        
        if inversion_count % 2 == 0: inversions_even = True
        else: inversions_even = False

        if width % 2 == 0: width_even = True
        else: width_even = False

        # our zero_location tuple counts rows from the top,
        # but this algorithm needs to count from the bottom
        if width_even:
            zero_odd = not y_is_even
        # if width not even, we don't need zero_odd (see docstring links)
        
        # see the bham.ac.uk link
        return ((not width_even and inversions_even)
               or
               (width_even and (zero_odd == inversions_even)))
