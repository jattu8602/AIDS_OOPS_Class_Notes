
# Python vs Prolog: A Comparison

# Introduction:
# Python and Prolog are both high-level programming languages, but they belong to different paradigms.
# Python is a multi-paradigm language that supports procedural, object-oriented, and functional programming.
# Prolog is a logic programming language used primarily for AI and symbolic reasoning, especially in domains like natural language processing, databases, and expert systems.

# History:
# Python: Created by Guido van Rossum and first released in 1991, Python was designed to be simple and easy to understand, with readable syntax.
# Prolog: Developed in the early 1970s by Alain Colmerauer and Robert Kowalski, Prolog (PROgramming in LOGic) is rooted in formal logic and often used for tasks involving symbolic reasoning.

# Core Differences:
# - Python focuses on explicit control of the program flow with step-by-step instructions.
# - Prolog is declarative, where you define facts and rules, and the Prolog engine solves problems based on logical inference.

# Problem Example: Water Jug Problem
# In Python, we explicitly define the state transitions and use search algorithms (BFS/DFS).
# In Prolog, we define facts and rules, and the language's inference engine automatically finds the solution.

# Python Solution (BFS):
from collections import deque

def bfs_solution(max_x, max_y, goal):
    start_state = (0, 0)
    queue = deque([(start_state, [])])  # queue holds (current_state, path)
    visited = set([start_state])  # to avoid revisiting states

    while queue:
        current_state, path = queue.popleft()

        if current_state[0] == goal or current_state[1] == goal:
            return path + [current_state]

        x, y = current_state
        next_states = [
            (max_x, y),  # Fill X
            (x, max_y),  # Fill Y
            (0, y),      # Empty X
            (x, 0),      # Empty Y
            (x - min(x, max_y - y), y + min(x, max_y - y)),  # Pour X to Y
            (x + min(y, max_x - x), y - min(y, max_x - x))   # Pour Y to X
        ]

        for next_state in next_states:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))

    return None  # No solution found

# Usage example in Python
jug_x_capacity = 5
jug_y_capacity = 3
goal_amount = 4

bfs_solution_path = bfs_solution(jug_x_capacity, jug_y_capacity, goal_amount)
if bfs_solution_path:
    print("Python BFS Solution:", bfs_solution_path)
else:
    print("No solution found with Python.")

# Prolog Solution:
# In Prolog, we define the facts (jug capacities) and rules (operations like fill, empty, and pour).
# Prolog will infer the solution based on these definitions.

'''
Prolog Code:
--------------------------------
% Define the jug capacities
capacity(5, 3).

% Define the possible operations: fill, empty, pour
move((X, Y), (5, Y)) :- X < 5.         % Fill jug X
move((X, Y), (X, 3)) :- Y < 3.         % Fill jug Y
move((X, Y), (0, Y)) :- X > 0.         % Empty jug X
move((X, Y), (X, 0)) :- Y > 0.         % Empty jug Y
move((X, Y), (X1, Y1)) :- X > 0, Y < 3, Transfer is min(X, 3 - Y), X1 is X - Transfer, Y1 is Y + Transfer.  % Pour X to Y
move((X, Y), (X1, Y1)) :- Y > 0, X < 5, Transfer is min(Y, 5 - X), X1 is X + Transfer, Y1 is Y - Transfer.  % Pour Y to X

% Goal state: one of the jugs has 4 liters
goal((4, _)).
goal((_, 4)).

% BFS search for solution
solve_bfs([State | Path], [State | Path]) :- goal(State).
solve_bfs([State | Path], Solution) :-
    move(State, NextState),
    \+ member(NextState, Path),
    solve_bfs([NextState, State | Path], Solution).

% Query to find the solution:
% ?- solve_bfs([(0, 0)], Solution).
--------------------------------
'''

# Differences Between Python and Prolog:
# 1. Paradigm:
#    - Python: Procedural (explicit control of the program flow).
#    - Prolog: Declarative (define rules and facts, Prolog solves the problem logically).
#
# 2. Control:
#    - Python: Requires manual implementation of search algorithms (BFS, DFS, etc.).
#    - Prolog: Built-in logical inference engine to automatically explore solutions.
#
# 3. Syntax:
#    - Python: Uses a straightforward, readable syntax. State changes and operations are written as code logic.
#    - Prolog: Uses predicates and logical rules. The problem-solving process is based on facts and rules.
#
# 4. Usage:
#    - Python: Widely used for general-purpose programming, from web development to AI and data science.
#    - Prolog: Primarily used in AI, especially for tasks like expert systems, natural language processing, and solving logical puzzles.

# Conclusion:
# Python is flexible and beginner-friendly, but requires explicit control for problem-solving.
# Prolog is specialized in logic-based problem-solving, making it a great choice for symbolic reasoning and AI tasks that require inference.
