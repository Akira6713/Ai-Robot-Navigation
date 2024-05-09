# Robot Navigation with A* Search

This project explores the foundations of robot navigation in a simulated grid-based environment, using the A* search algorithm. It serves as a step towards understanding the complexities of AI-powered movement in the physical world. It highlights the importance of efficient and reliable pathfinding algorithms for navigating physical spaces. As we develop increasingly sophisticated robots, pathfinding solutions will need to adapt to complex, dynamic environments and leverage more advanced AI techniques.

## Image of sample Robot path using matplotlib
![Robot-Path](https://github.com/Akira6713/robot-navigation/assets/66973202/19b7c159-fbcd-4b24-a314-08549b3f960c)

## Overview

The robot navigation system aims to find an optimal path for a simulated robot to travel from a starting point to a goal position within a map containing obstacles.

## Problem Description

- The robot exists on a 2D grid map.
- Obstacles (e.g., walls, objects) are represented as impassable cells on the grid.
- The robot can move to adjacent open cells in four directions (up, down, left, right).
- The goal is to find the shortest obstacle-free path from the robot's starting position to a designated goal cell.

## Solution Approach

The project implements the A* search algorithm to solve this pathfinding problem. A* is an informed search algorithm that leverages the following:

- **Cost so far:** The distance traveled from the start.
- **Heuristic estimate:** An approximation of the distance remaining to the goal (in this case, we use the Manhattan distance).

## Justification for A* Search

- **Completeness:** A* guarantees finding an optimal solution if a path exists.
- **Admissibility:** With the distance heuristic, A* never overestimates the cost to the goal, ensuring optimality.
- **Trade-offs:** A* can become memory-intensive for very large maps or complex environments.

## Usage Instructions

**Dependencies:**

- Python 3
- simpleai
- matplotlib

**Visualization:**

If a path is found, a Matplotlib plot will display the map, the robot's start and goal, and the calculated path.

## Example

**Sample MAP:**

[0, 0, 0, 1]
[1, 0, 0, 0]
[0, 0, 1, 0]
[0, 0, 0, 0]


- `0` represents an open cell.
- `1` represents an obstacle.

**START:** (0, 0)

**GOAL:** (3, 2)
