import numpy as np
import cv2
import random

def show(maze,wait=0):
	scaled_image = cv2.resize(maze, None, fx=5, fy=5, interpolation=cv2.INTER_NEAREST)
	cv2.imshow('Scaled Image', scaled_image)
	cv2.waitKey(wait)
	
maze = np.zeros((51, 51), dtype=np.uint8)
maze[1::2,1::2]=150

def get_neighbors(point,maze):
	y,x=point
	neighbors=[]
	h,w=maze.shape[:2]
	for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
		yp=y+2*dy
		xp=x+2*dx
		if xp<0 or yp<0 or xp>w-1 or yp>h-1 or maze[yp,xp]==255:
			continue
		neighbors.append((yp,xp))
	return neighbors	

def get_good_neighbors(point,maze):
	y,x=point
	neighbors=[]
	h,w=maze.shape[:2]
	for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
		yp=y+2*dy
		xp=x+2*dx
		xm=(x+xp)//2
		ym=(y+yp)//2
		if xp<0 or yp<0 or xp>w-1 or yp>h-1 or maze[ym,xm]==0:
			continue
		neighbors.append((yp,xp))
	return neighbors	


deque=[(1,1)]

# Growing Tree Maze Generation
deque = [(25, 25)]
while deque:
    index = random.randrange(len(deque))
    current_cell = deque[index]
    y, x = current_cell
    neighbors = get_neighbors(current_cell, maze)
    if neighbors:
        next_cell = random.choice(neighbors)
        ny, nx = next_cell
        maze[ny, nx] = 255
        maze[(y + ny) // 2, (x + nx) // 2] = 255
        deque.append(next_cell)
        show(maze, 10) 
    else:
        deque.pop(index)
show(maze)
cv2.destroyAllWindows()

deque=[(1,1)]

# Create video writer
out = cv2.VideoWriter('TreeSeward.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, (255, 255))

while deque:
	index=random.randrange(len(deque))
	node=deque[index]
	y,x=node
	neighbors=get_neighbors(node,maze)
	if neighbors:
		y2,x2=random.choice(neighbors)
		maze[y,x]=255
		maze[y2,x2]=255
		maze[(y2+y)//2,(x2+x)//2]=255
		deque.append((y2,x2))
		show(maze,10)
	else:
		deque.pop(index)

h, w = maze.shape[:2]
location = (1, 1)
target = (h - 2, w - 2)
m = cv2.cvtColor(maze, cv2.COLOR_GRAY2BGR)

while location != target:
    location = random.choice(get_good_neighbors(location, maze))
    m[location] = (255, 0, 0)
    scaled_image = cv2.resize(m, None, fx=5, fy=5, interpolation=cv2.INTER_NEAREST)
    out.write(scaled_image)  # Write frame to video
    cv2.imshow('Scaled Image', scaled_image)
    cv2.waitKey(5)

out.release()  # Release video writer
cv2.destroyAllWindows()