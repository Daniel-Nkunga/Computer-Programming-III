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


# deque=[(1,1)]

# DFS Maze Generation (Seward)
# while deque:
# 	index=random.randrange(len(deque))
# 	node=deque[index]
# 	y,x=node
# 	neighbors=get_neighbors(node,maze)
# 	if neighbors:
# 		y2,x2=random.choice(neighbors)
# 		maze[y,x]=255
# 		maze[y2,x2]=255
# 		maze[(y2+y)//2,(x2+x)//2]=255
# 		deque.append((y2,x2))
# 		show(maze,10)
# 	else:
# 		deque.pop(index)

# cv2.destroyAllWindows()
# h,w=maze.shape[:2]
# location=(1,1)
# direction=(2,0)
# show(maze)

# # Growing Tree Maze Generation
# deque = [(25, 25)]
# while deque:
#     index = random.randrange(len(deque))
#     current_cell = deque[index]
#     y, x = current_cell
#     neighbors = get_neighbors(current_cell, maze)
#     if neighbors:
#         next_cell = random.choice(neighbors)
#         ny, nx = next_cell
#         maze[ny, nx] = 255
#         maze[(y + ny) // 2, (x + nx) // 2] = 255
#         deque.append(next_cell)
#         show(maze, 10) 
#     else:
#         deque.pop(index)
# show(maze)
# cv2.destroyAllWindows()

# Kurksal's Algorithm
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

def kruskal_maze(maze):
    h, w = maze.shape[:2]
    edges = []
    for y in range(1, h - 1, 2):
        for x in range(1, w - 1, 2):
            if x + 2 < w - 1:
                edges.append((random.random(), (y, x), (y, x + 2)))
            if y + 2 < h - 1:
                edges.append((random.random(), (y, x), (y + 2, x)))
    edges.sort()
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
            show(maze, 1)

maze = np.zeros((51, 51), dtype=np.uint8)
maze[1::2, 1::2] = 255
kruskal_maze(maze)
cv2.destroyAllWindows()
show(maze)

deque=[(1,1)]
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

