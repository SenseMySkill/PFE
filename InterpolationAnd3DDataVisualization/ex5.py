import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from PIL import Image

img = np.array(Image.open("img2.png").convert("L"))

points = np.column_stack(np.nonzero(img > 0))
values = img[img > 0]

# siatka do rekonstrukcji
grid_x, grid_y = np.mgrid[0:img.shape[0]:500j, 0:img.shape[1]:500j]

# interpolacja 2D
recon = griddata(points, values, (grid_x, grid_y), method='cubic', fill_value=0)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Oryginalne punkty")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(recon, cmap='gray')
plt.title("Rekonstrukcja (cubic interpolation)")
plt.axis("off")

plt.show()
