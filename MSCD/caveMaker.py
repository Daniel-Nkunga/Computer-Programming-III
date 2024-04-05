import numpy as np
import cv2
import csv
import time
from collections import deque

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

def pce(cave, x, y, z, size = 41, wall = 5):
     a = np.sum(cave[x - size // 2 : x + size // 2 + 1,
                     y - size // 2 : y + size // 2 + 1,
                     z - size // 2 : z + size // 2 + 1])

     b = np.sum(cave[x - size // 2 - wall : x + size // 2 + 1 + wall,
                     y - size // 2 - wall : y + size // 2 + 1 + wall, 
                     z - size // 2 - wall : z + size // 2 + 1 + wall])
     full = b
     interior = a
     pc = 63730 #perfect cave = pc
     cost = (interior + max(pc - full, 0)) * 2
     return cost

def preserveDirt(cave, x, y, z, missing, fill_value = 1, size = 41, wall = 5, buff = 5, replace = 0):
     if missing < 0:
          fill_value = 0
          missing = abs(missing)
          replace = 1
     seed = [x - size - wall, y - size - wall, z - size - wall]
     while cave[*seed] != replace: 
        seed[0] += 1
     queue = deque([tuple(seed)])
     filled = np.zeros_like(cave, dtype = bool)
     filled[seed] = True

     while queue and missing > 0:
          i, j, k = queue.popleft()
          
          if cave[i, j, k] == fill_value:
               continue
          cave[i, j, k] = fill_value
          missing -= 1

          neighbors = [(i + 1, j, k), (i, j + 1, k)]
        
          for nx, ny, nz in neighbors:
            if 0 <= nx < cave.shape[0] and 0 <= ny < cave.shape[1] and 0 <= nz < cave.shape[2]:
                 if not filled[nx, ny, nz] and cave[nx, ny, nz] == replace:
                    queue.append((nx, ny, nz))
                    filled[nx, ny, nz] = True

     return missing

cave=loadCave("input.cave")
start=time.time()
ogCave=cave*1
size=41
wall=5
buff=5
x, y, z, = 256, 275, 460

# Best Coordinates
# 239, 275, 460
# 441, 476, 163
# 365, 032, 248
# 210, 061, 247
# 444, 273, 462
# 143, 266, 262
# 121, 296, 186

print("dirt former",cave.sum())
saveCave(cave,"output.cave")
# x, y, z, = 239, 275, 460 #[Beautiful Bungalow]
# cave[x - size // 2 - wall : x + size // 2 + 1 + wall,
#      y - size // 2 - wall : y + size // 2 + 1 + wall, 
#      z - size // 2 - wall : z + size // 2 + 1 + wall] = 1
# cave[x - size // 2 : x + size // 2 + 1, 
#      y - size // 2 : y + size // 2 + 1, 
#      z - size // 2 : z + size // 2 + 1] = 0
# x, y, z, = 441, 476, 163 #[Lovely Lodge]
# cave[x - size // 2 - wall : x + size // 2 + 1 + wall,
#      y - size // 2 - wall : y + size // 2 + 1 + wall, 
#      z - size // 2 - wall : z + size // 2 + 1 + wall] = 1
# cave[x - size // 2 : x + size // 2 + 1, 
#      y - size // 2 : y + size // 2 + 1, 
#      z - size // 2 : z + size // 2 + 1] = 0
x, y, z, = 365, 32, 248 #[The Bad One; it doesn't work]
cave[x - size // 2 - wall : x + size // 2 + 1 + wall,
     y - size // 2 - wall : y + size // 2 + 1 + wall, 
     z - size // 2 - wall : z + size // 2 + 1 + wall] = 1
cave[x - size // 2 : x + size // 2 + 1, 
     y - size // 2 : y + size // 2 + 1, 
     z - size // 2 : z + size // 2 + 1] = 0
# x, y, z, = 210, 61, 247 #[Gorgeous Getaway]
# cave[x - size // 2 - wall : x + size // 2 + 1 + wall,
#      y - size // 2 - wall : y + size // 2 + 1 + wall, 
#      z - size // 2 - wall : z + size // 2 + 1 + wall] = 1
# cave[x - size // 2 : x + size // 2 + 1, 
#      y - size // 2 : y + size // 2 + 1, 
#      z - size // 2 : z + size // 2 + 1] = 0
# x, y, z, = 444, 273, 462 #[Shameful Shack]
# cave[x - size // 2 - wall : x + size // 2 + 1 + wall,
#      y - size // 2 - wall : y + size // 2 + 1 + wall, 
#      z - size // 2 - wall : z + size // 2 + 1 + wall] = 1
# cave[x - size // 2 : x + size // 2 + 1, 
#      y - size // 2 : y + size // 2 + 1, 
#      z - size // 2 : z + size // 2 + 1] = 0
# x, y, z, = 143, 266, 262 #[Radiant Residence]
# cave[x - size // 2 - wall : x + size // 2 + 1 + wall,
#      y - size // 2 - wall : y + size // 2 + 1 + wall, 
#      z - size // 2 - wall : z + size // 2 + 1 + wall] = 1
# cave[x - size // 2 : x + size // 2 + 1, 
#      y - size // 2 : y + size // 2 + 1, 
#      z - size // 2 : z + size // 2 + 1] = 0

missing = 84504414 - cave.sum()
preserveDirt(cave, x, y, z, missing)
# saveCave(cave, "EtherealEstate_121_296_186_41282_nkungad.cave")
saveCave(cave, "Test.cave")
# print(missing)
print("cost",np.abs(cave*1.0-ogCave).sum() )
print("dirt latter",cave.sum())
print(x, y, z)
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






