import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import random

seedLen = random.randint(1,5)
seed = ''
for i in range(seedLen):
    seed += str(random.randint(1, 9))

seed = int(seed)

noise = PerlinNoise(octaves=8, seed=seed)
xlen = 200
ylen = 200

pic = []

def createNoise():
    for i in range(xlen):
        row = []
        for j in range(ylen):
            row.append([noise([i/xlen, j/ylen])])
        pic.append(row)
    return pic

print(seed)
pic = createNoise()
plt.imshow(pic, cmap='gray')
plt.show()