import numpy as np
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt

colourmap = {
    -0.1 : [(0,0,0), 'darkstone'],
    0.05 : [(20,20,20), 'lightstone'],
    0.2 : [(255,255,255), 'air']
}

def generate_perlin_noise(width, height, scale=1):
    """
    Generates a Perlin noise grid.
    :param width: Width of the noise grid.
    :param height: Height of the noise grid.
    :param scale: The scale of the noise (higher values create more zoomed-out noise).
    :return: A 2D numpy array of Perlin noise values.
    """
    noise_instance = PerlinNoise(octaves=2, seed=36174324)
    noise_grid = np.zeros((height, width))
    for y in range(height):
        for x in range(width):
            noise_grid[y][x] = noise_instance([x / scale, y / scale])
    return noise_grid

def getColour(value):
    for threshold, colour in sorted(colourmap.items()):
        if value < threshold:
            return colour
    return colourmap[max(colourmap.keys())]
        
def mapColour(noiseGrid):
    height, width = noiseGrid.shape
    colourImage = np.zeros((height, width, 3), dtype=np.uint8)
    types = np.full((height, width, 1), "", dtype=object)

    for x in range(width):
        for y in range(height):
            colourImage[y][x] = getColour(noiseGrid[y][x])[0]
            types[y][x] = getColour(noiseGrid[y][x])[1]

    return colourImage, types

if __name__ == "__main__":
    width, height = 100,500
    perlin_noise = generate_perlin_noise(width, height, scale=30)
    
    colourImage = mapColour(perlin_noise)[0]
    types = mapColour(perlin_noise)[1]
    print(types)

    plt.imshow(colourImage)
    plt.show()