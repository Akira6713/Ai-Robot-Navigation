# Robot Navigation using A* Search algorithm

from simpleai.search import astar, SearchProblem
import matplotlib.pyplot as plt

MAP = [
    [0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0]
]

START = (0, 0)  # Robot's starting position
GOAL = (7, 6)  # Goal position

class RobotProblem(SearchProblem):
    def actions(self, state):
        actions = []
        x, y = state
        # Check for movement upwards
        if x > 0 and MAP[x - 1][y] == 0:
            actions.append('Up')
        # Check for movement to the left
        if y > 0 and MAP[x][y - 1] == 0:
            actions.append('Left')
        # Check for movement downwards
        if x < len(MAP) - 1 and MAP[x + 1][y] == 0:
            actions.append('Down')
        # Check for movement to the right
        if y < len(MAP[0]) - 1 and MAP[x][y + 1] == 0:
            actions.append('Right')
        return actions

    def result(self, state, action):
        x, y = state

        # Calculate the new state based on the chosen action
        if action == 'Up':
            return x - 1, y  # Move Up
        if action == 'Left':
            return x, y - 1  # Move Left
        if action == 'Down':
            return x + 1, y  # Move Down
        if action == 'Right':
            return x, y + 1  # Move Right

    def is_goal(self, state):
        # Check if the current state matches the goal state
        return state == GOAL

    def heuristic(self, state):
        x, y = state
        gx, gy = GOAL
        # Estimate of distance to the goal
        return abs(x - gx) + abs(y - gy)

def visualize_path(map, path):
    # Check for an empty path (no solution found)
    if not path:
        print("No valid path found to the goal.")
        return

    print("Path found:", path)

    # Set up Matplotlib plot
    fig, ax = plt.subplots()
    ax.imshow(map, cmap='gray')

    # Extract coordinates from the path and plot them
    path_coords = [(state[1][0], state[1][1]) for state in path if state[0] is not None]
    path_x, path_y = zip(*path_coords)

    # Plot start and goal markers
    ax.plot(path_y, path_x, color='red', marker='o', linestyle='-')
    ax.plot(path_y[0], path_x[0], 'bs', markersize=12)
    ax.plot(path_y[-1], path_x[-1], 'gs', markersize=12)

    # Add labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Robot Navigation Path')
    plt.show()


problem = RobotProblem(START)
result = astar(problem)
visualize_path(MAP, result.path())
print(result.path())
