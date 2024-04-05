import cv2
import numpy as np

# Load the maze image
maze_image = cv2.imread('TargetMaze.png', cv2.IMREAD_COLOR)

# Convert the image to RGB format
maze_image_rgb = cv2.cvtColor(maze_image, cv2.COLOR_BGR2RGB)

# Extract unique colors from the image
unique_colors = np.unique(maze_image_rgb.reshape(-1, maze_image_rgb.shape[2]), axis=0)

# Print the RGB values of each unique color
for color in unique_colors:
    print("RGB:", color)
