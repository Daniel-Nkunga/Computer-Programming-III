import cv2
import numpy as np
import heapq

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def astar(array, start, goal, maze_image):
    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []

    out = cv2.VideoWriter('test.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (640, 640)) # Video writer object
    
    heapq.heappush(oheap, (fscore[start], start))
    
    while oheap:
        current = heapq.heappop(oheap)[1]
        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            data.append(start)
            return data
        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j            
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:                
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    continue
            else:
                continue
                
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
                
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))
                # Mark the explored nodes with a different color (green)
                maze_image[neighbor[0], neighbor[1]] = [0, 255, 0]
                
        # Display the current state of the maze with explored nodes and frontier
        maze_image_display = maze_image.copy()
        for item in oheap:
            maze_image_display[item[1][0], item[1][1]] = [255, 255, 0]  # Mark frontier nodes with yellow color
        
        # Resize the image for better visualization
        maze_image_resized = cv2.resize(maze_image_display, (640, 640))  # Resize to 640x640
        
        # Write the frame to the video
        out.write(maze_image_resized)
    
    out.release() # Release the video writer
    return False

# Load the maze image
maze_image = cv2.imread('BWMaze.png', cv2.IMREAD_COLOR)

# Threshold the image to get binary values (0 and 255)
ret, thresh = cv2.threshold(maze_image, 127, 255, cv2.THRESH_BINARY)

# Invert the binary image so that walls are 1s and paths are 0s
maze_array = 1 - (thresh[:, :, 0] / 255)

# Define start and end points
start = (0, 0)
end = (127, 127)

# Run A* algorithm to find the path and visualize the search process
path = astar(maze_array, start, end, maze_image)

if path:
    print("Path found!")
    print(path)
    # Mark the final path on the maze image
    for position in path:
        maze_image[position[0], position[1]] = [255, 0, 0]  # Set path pixels to blue
    
    # Resize the image for better visualization
    maze_image_resized = cv2.resize(maze_image, (640, 640))  # Resize to 640x640
    
    # Save the final image with the path
    cv2.imwrite("Maze_with_Path.png", maze_image_resized)
    
    # Show the final image with the path
    cv2.imshow("Maze with Path", maze_image_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("No path found!")
