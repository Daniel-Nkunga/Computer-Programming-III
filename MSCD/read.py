import numpy as np
import cv2

def makePretty(img):
    out = np.zeros((512, 512, 3), dtype=np.uint8)
    out[img == 0] = (255, 200, 200)
    out[img == 1] = (40, 60, 100)
    return out

def loadCave(filename):
    cave_bytes = np.fromfile(filename, dtype=np.uint8)
    cave_bits = np.unpackbits(cave_bytes)
    cave = np.reshape(cave_bits, (512, 512, 512))
    return cave

def saveCave(cave, filename):
    np.packbits(np.uint8(np.ravel(cave))).tofile(filename)

def place_dirt(cave, x, y, z):
    cave[x, y, z] = 1

def ensure_dirt_consistency(cave, ogCave, dirtBefore):
    dirtAfter = cave.sum()
    dirtMissing = dirtBefore - dirtAfter
    if dirtMissing > 0:
        # If there is missing dirt, iterate through the original cave and add it back
        for x in range(512):
            for y in range(512):
                for z in range(512):
                    if ogCave[x, y, z] == 1 and cave[x, y, z] == 0:
                        place_dirt(cave, x, y, z)
                        dirtMissing -= 1
                        if dirtMissing == 0:
                            return

cave = loadCave("input.cave")
import time
start = time.time()
ogCave = cave * 1
# Make a mock burrow. I didn't conserve dirt.
print("dirt before", ogCave.sum())
dirtBefore = ogCave.sum()
x, y, z = 256, 256, 256
size = 41
wall = 5
cave[x - size // 2 - wall:x + size // 2 + 1 + wall,
     y - size // 2 - wall:y + size // 2 + 1 + wall,
     z - size // 2 - wall:z + size // 2 + 1 + wall] = 1
cave[x - size // 2:x + size // 2 + 1,
     y - size // 2:y + size // 2 + 1,
     z - size // 2:z + size // 2 + 1] = 0

saveCave(cave, "output.cave")
ensure_dirt_consistency(cave, ogCave, dirtBefore)
saveCave(cave, "output.cave")
print("cost", np.abs(cave * 1.0 - ogCave).sum())
print("dirt after", cave.sum())
dirtMissing = (dirtBefore - cave.sum())

end = time.time()
print(end - start)

#Push