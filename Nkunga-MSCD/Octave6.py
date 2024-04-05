import numpy as np
import cv2
import csv
import time

def makePretty(img):
    out=np.zeros((512,512,3),dtype=np.uint8)
    out[img==0]=(255,200,200)
    out[img==1]=(40,60,100)
    return out

def loadCave(filename):
    cave_bytes=np.fromfile(filename, dtype=np.uint8)
    cave_bits=np.unpackbits(cave_bytes)
    cave=np.reshape(cave_bits,(512,512,512))
    return cave

def saveCave(cave,filename):
	np.packbits(np.uint8(np.ravel(cave))).tofile(filename)

def cost(cave, x, y, z, size=51, wall=5):
    # Calculate the sum of dirt inside the burrow
    interior = np.sum(cave[x - size // 2: x + size // 2 + 1,
                          y - size // 2: y + size // 2 + 1,
                          z - size // 2: z + size // 2 + 1])
    
    # Calculate the sum of dirt in the surrounding wall
    walls = np.sum(cave[x - size // 2 - wall: x + size // 2 + 1 + wall,
                        y - size // 2 - wall: y + size // 2 + 1 + wall,
                        z - size // 2 - wall: z + size // 2 + 1 + wall])
    
    # Calculate the cost based on the interior and wall dirt sums
    total_dirt = interior + walls
    
    # Calculate the missing dirt based on the constraint
    missing_dirt = 84_504_414 - cave.sum()
    
    # Calculate the cost based on the absolute difference between start and end points
    cost = np.abs(total_dirt - missing_dirt)
    
    return cost, missing_dirt

def pce(cave, x, y, z, size = 41, wall = 5):
     a = np.sum(cave[x - size // 2 : x + size // 2 + 1,
                     y - size // 2 : y + size // 2 + 1,
                     z - size // 2 : z + size // 2 + 1])

     b = np.sum(cave[x - size // 2 - wall : x + size // 2 + 1 + wall,
                     y - size // 2 - wall : y + size // 2 + 1 + wall, 
                     z - size // 2 - wall : z + size // 2 + 1 + wall])
    #  print(b)
     full = b
     interior = a
     pc = 63730 #perfect cave = pc
     cost = (interior + max(pc - full, 0)) * 2
     return cost

cave=loadCave("input.cave")
start=time.time()
ogCave=cave*1
size=51
wall=5
buff=5

x, y, z, = 45, 45, 45

#250 350 400 83650

results = []
for i in range(257, 512, 1):
    for j in range(0, 256, 1):
        for k in range(257, 512, 1):
            if pce(cave, i, j, k) <= 43_500:
                print(pce(cave, i, j, k))
                results.append((i, j, k, pce(cave, i, j, k)))
with open('Octave6.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['X', 'Y', 'Z', 'Cost'])
    writer.writerows(results)

saveCave(cave,"output.cave")
# print("cost",np.abs(cave*1.0-ogCave).sum() )
# print("dirt after",cave.sum())
end=time.time()
# print(results)
print(end-start)

#sliders can't hit every number
def side_change(val):
    cv2.imshow("side view", makePretty(cave[:,val,:].T))
cv2.imshow("side view", makePretty(cave[:,0,:].T))
cv2.createTrackbar('slider', "side view", 0, 511, side_change)
def top_change(val):
    cv2.imshow("top view", makePretty(cave[:,:,val]))
cv2.imshow("top view", makePretty(cave[:,:,0].T))
cv2.createTrackbar('slider', "top view", 0, 511, top_change)
cv2.waitKey(0)