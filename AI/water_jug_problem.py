
# Water Jug Problem: Solving with BFS and DFS
# ---------------------------------------------------
# The water jug problem is a classic problem in AI. The problem consists of two jugs with fixed capacities,
# and the goal is to measure out an exact amount of water using just these jugs and basic operations like fill, empty, and pour.
#
# Example Problem:
# You are given two jugs: Jug X with a capacity of 5 liters, and Jug Y with a capacity of 3 liters.
# You must measure exactly 4 liters of water using the jugs.
#
# Operations:
# - Fill a jug to its full capacity.
# - Empty a jug.
# - Pour water from one jug into the other until one is either full or the other is empty.

from collections import deque

# Function to check if the goal state is reached
def is_goal_state(state, goal):
    return state[0] == goal or state[1] == goal

# Generate possible next states
def get_next_states(state, max_x, max_y):
    x, y = state
    next_states = []

    # Fill jug X or Y
    next_states.append((max_x, y))  # Fill X
    next_states.append((x, max_y))  # Fill Y

    # Empty jug X or Y
    next_states.append((0, y))  # Empty X
    next_states.append((x, 0))  # Empty Y

    # Pour from X to Y
    transfer_x_to_y = min(x, max_y - y)
    next_states.append((x - transfer_x_to_y, y + transfer_x_to_y))

    # Pour from Y to X
    transfer_y_to_x = min(y, max_x - x)
    next_states.append((x + transfer_y_to_x, y - transfer_y_to_x))

    return next_states

# BFS solution
def bfs_solution(max_x, max_y, goal):
    start_state = (0, 0)
    queue = deque([(start_state, [])])  # queue holds (current_state, path)
    visited = set([start_state])  # to avoid revisiting states

    while queue:
        current_state, path = queue.popleft()

        if is_goal_state(current_state, goal):
            return path + [current_state]

        for next_state in get_next_states(current_state, max_x, max_y):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))

    return None  # No solution found

# DFS solution (recursive)
def dfs_solution(max_x, max_y, goal, current_state=(0, 0), path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path.append(current_state)
    visited.add(current_state)

    if is_goal_state(current_state, goal):
        return path

    for next_state in get_next_states(current_state, max_x, max_y):
        if next_state not in visited:
            result = dfs_solution(max_x, max_y, goal, next_state, path[:], visited)
            if result:
                return result

    return None

# Example Usage
if __name__ == "__main__":
    # Jug capacities: 5 liters and 3 liters, with a goal of 4 liters
    jug_x_capacity = 5
    jug_y_capacity = 3
    goal_amount = 4

    print("BFS Solution:")
    bfs_solution_path = bfs_solution(jug_x_capacity, jug_y_capacity, goal_amount)
    if bfs_solution_path:
        for step in bfs_solution_path:
            print(step)
    else:
        print("No solution found with BFS.")

    print("\nDFS Solution:")
    dfs_solution_path = dfs_solution(jug_x_capacity, jug_y_capacity, goal_amount)
    if dfs_solution_path:
        for step in dfs_solution_path:
            print(dfs_solution_path)
    else:
        print("No solution found with DFS.")
