import numpy as np
import cv2

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


cave=loadCave("input.cave")
import time
start=time.time()
ogCave=cave*1
#Make a mock burrow.  I didn't conserve dirt.
print("dirt before",ogCave.sum())
# print("air before",(1-ogCave).sum())
x,y,z=256,256,256
size=41
wall=5
# buff=5
# cave[x-size//2-wall:x+size//2+1+wall,
#      y-size//2-wall:y+size//2+1+wall,
#      z-size//2-wall:z+size//2+1+wall]=1
# cave[x-size//2:x+size//2+1,
#      y-size//2:y+size//2+1,
#      z-size//2:z+size//2+1]=0
for i in range(0, x, 75):
     for j in range(0, y, 75):
          for k in range(0, z, 75):
            cave[i:i + size + wall,
                 j:j + size + wall,
                 k:k + size + wall]=1
            cave[i + wall:i + size,
                 j + wall:j + size,
                 k + wall:k + size]=0
            if(np.abs(cave*1.0-ogCave).sum() <= 40_000):
                print(f"good cost at {i}, {j}, {k}")
                cave = ogCave * 1
                saveCave(cave, "output.cave")
            else:
                cave = ogCave * 1
                # print("too expensive")
                saveCave(cave, "output.cave")

# #Test Cave
# cave[0:0 + size + wall,
#     0:0 + size + wall,
#     0:0 + size + wall]=1
# cave[0 + wall:0 + size,
#         0 + wall:0 + size,
#         0 + wall:0 + size]=0

# saveCave(cave,"output.cave")
print("cost",np.abs(cave*1.0-ogCave).sum() )
print("dirt after",cave.sum())
end=time.time()
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