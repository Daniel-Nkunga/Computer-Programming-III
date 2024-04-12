import numpy as np
import cv2
import random

def show_maze(maze, wait=1):
    scaled_image = cv2.resize(maze, None, fx=20, fy=20, interpolation=cv2.INTER_NEAREST)
    cv2.imshow('Maze', scaled_image)
    cv2.waitKey(wait)

def is_valid_move(maze, row, col, visited):
    num_rows, num_cols = maze.shape[:2]
    
    # Check if the move is within the bounds of the maze
    if row < 0 or row >= num_rows or col < 0 or col >= num_cols:
        return False
    
    # Check if the move hits a wall or has been visited before
    if maze[row, col] == 0 or visited[row, col]:
        return False
    
    return True

def dfs(maze, visited, row, col, target, path):
    # If current cell is the target, return True to indicate path found
    if (row, col) == target:
        return True
    
    # Mark current cell as visited
    visited[row, col] = True
    
    # Possible movements: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        
        if is_valid_move(maze, new_row, new_col, visited):
            path.append((new_row, new_col))
            show_maze(visited.astype(np.uint8) * 255)  # Show visited cells
            if dfs(maze, visited, new_row, new_col, target, path):
                return True
            path.pop()  # Backtrack if no valid path found
    
    return False

def solve_maze(maze, start, target):
    num_rows, num_cols = maze.shape[:2]
    
    # Initialize visited array
    visited = np.zeros_like(maze, dtype=bool)
    
    # Initialize path with start position
    path = [start]
    
    # Use DFS to find a path from start to target
    if dfs(maze, visited, start[0], start[1], target, path):
        return path
    else:
        return []

def kruskal_maze(maze):
    h, w = maze.shape[:2]
    edges = []
    
    # Collect all potential edges
    for y in range(1, h - 1, 2):
        for x in range(1, w - 1, 2):
            if x + 2 < w - 1:
                edges.append((random.random(), (y, x), (y, x + 2)))
            if y + 2 < h - 1:
                edges.append((random.random(), (y, x), (y + 2, x)))
    
    # Sort edges based on weight
    edges.sort()
    
    # Kruskal's Algorithm to generate maze
    parent = {}
    rank = {}
    for y in range(1, h - 1, 2):
        for x in range(1, w - 1, 2):
            parent[(y, x)] = (y, x)
            rank[(y, x)] = 0
    
    for weight, (y1, x1), (y2, x2) in edges:
        root1 = find(parent, (y1, x1))
        root2 = find(parent, (y2, x2))

        if root1 != root2:
            if x1 == x2:
                maze[(y1 + y2) // 2, x1] = 255
            elif y1 == y2: 
                maze[y1, (x1 + x2) // 2] = 255

            union(parent, rank, root1, root2)
            show_maze(maze)
            cv2.waitKey(1)

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

# Main function to generate and solve maze
def main():
    # Initialize maze grid
    maze_size = (51, 51)  # Adjust maze size as needed
    maze = np.zeros(maze_size, dtype=np.uint8)
    maze[1::2, 1::2] = 255  # Initialize cells for maze generation
    
    # Generate maze using Kruskal's Algorithm
    kruskal_maze(maze)
    
    # Define start and target positions
    start = (1, 1)
    target = (maze_size[0] - 2, maze_size[1] - 2)
    
    # Solve maze using DFS
    path = solve_maze(maze, start, target)
    
    # Display maze with path
    maze_with_path = cv2.cvtColor(maze, cv2.COLOR_GRAY2BGR)
    if path:
        for pos in path:
            maze_with_path[pos] = (0, 255, 0)  # Mark path cells in green
            show_maze(maze_with_path)
            cv2.waitKey(50)  # Delay to visualize pathfinding
    show_maze(maze_with_path)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
