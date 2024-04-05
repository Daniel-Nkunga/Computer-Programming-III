import numpy as np
import cv2
import heapq

class PriorityQueue:
    def __init__(self):
        self.q = []
        self.lookup = {}
        self.i = 0

    def add(self, cost, elem): 
        if elem in self.lookup:
            if self.lookup[elem][0] > cost:
                self.remove(elem)
            else:
                return
        entry = [cost, -self.i, elem]
        self.i += 1
        heapq.heappush(self.q, entry)
        self.lookup[elem] = entry

    def pop(self):
        elem = False
        while not elem:
            cost, _, elem = heapq.heappop(self.q)   
        self.lookup.pop(elem)
        return elem

    def remove(self, elem):
        entry = self.lookup.pop(elem)
        entry[-1] = False

    def __len__(self):
        return len(self.lookup)

def show(img, wait=10):
    img = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_NEAREST)  # Resize image to be 2x larger
    cv2.imshow("img", img)
    cv2.waitKey(wait)

def normalize(x):
    x = x * 1.0
    x -= x.min()
    x /= x.max()
    x *= 255.999
    return np.uint8(x)

def get_cost(_map, tile_coordinate): #This doesn't do anything yet
    y, x = tile_coordinate
    match _map[y][x]:
        case (255, 0, 0): return 15 #RED
        case (0, 0, 255): return 15 #BLUE
        case (0, 255, 0): return 15 #GREEN
        case (255, 255, 0): return 15 #YELLOW
        case (255, 255, 255): return 5 #WHITE
        case (0, 0, 0): return 255 #BLACK
        case _: return 240  # default case when color doesn't match any specified cases

map = cv2.imread(r"C:\Users\danie\Desktop\Coding Spring 2024\Computer-Programming-III\Pathfinding\Maze.png", 0)
show(map, 0)
h, w = map.shape

new_map = np.zeros_like(map)
for y in range(h):
    for x in range(w):
        new_map[y, x] = get_cost(map, (y, x))
# show(new_map, 0)

# costs = new_map
costs = map * 0.0 - 1

startx, starty = 0, 0
endx, endy = 64,64
costs[startx, starty] = 0

def heuristic(x, y):
    return 0

queue = PriorityQueue()
queue.add(0, (startx, starty))

i = 0
while queue:
    i += 1
    cx, cy = queue.pop()
    if cx == endx and cy == endy:
        break
    ccost = costs[cx, cy]
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        px = cx + dx
        py = cy + dy
        if px < 0 or px >= w or py < 0 or py >= h:
            continue
        pcost = ccost + map[px, py]
        if costs[px, py] == -1 or pcost < costs[px, py]:
            costs[px, py] = pcost
            queue.add(pcost + heuristic(px, py), (px, py))
            # Show exploration
            temp_map = map.copy()
            temp_map[px, py] = 100  # Highlight explored area
            show(normalize(costs), 1)

# Marble rolling algorithm (dynamic programming) to find the cheapest cost back
min_cost_path = np.zeros((w, h), dtype=np.float32) + np.inf
min_cost_path[endx, endy] = costs[endx, endy]  # Set cost at the end point
for x in range(endx, startx - 1, -1):
    for y in range(endy, starty - 1, -1):
        if x == endx and y == endy:
            continue
        min_cost_neighbors = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            px = x + dx
            py = y + dy
            if 0 <= px < w and 0 <= py < h:
                min_cost_neighbors.append(min_cost_path[px, py])
        if min_cost_neighbors:
            min_cost_path[x, y] = costs[x, y] + min(min_cost_neighbors)

# Find the path with minimum cost using dynamic programming result
x, y = startx, starty
min_cost_path_points = [(x, y)]
while (x, y) != (endx, endy):
    min_neighbor = min((min_cost_path[x + dx, y + dy], (dx, dy)) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)])
    dx, dy = min_neighbor[1]
    x += dx
    y += dy
    min_cost_path_points.append((x, y))

# Display the path in blue
for x, y in min_cost_path_points:
    map[x, y] = (255)  # Make the path blue

show(normalize(map), 0)