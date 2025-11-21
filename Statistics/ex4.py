import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.get_proj())
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)


data_flat = np.genfromtxt("PCAdata.txt")
data = data_flat.reshape(-1, 3)

mean = np.mean(data, axis=0)

cov_matrix = np.cov(data, rowvar=False)

eig_vals, eig_vecs = np.linalg.eig(cov_matrix)
print("eigenvalues:\n", eig_vals)
print("eigenvectors:\n", eig_vecs)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(data[:,0], data[:,1], data[:,2], c='green', s=50)

for i in range(len(eig_vals)):
    vec = eig_vecs[:,i] * np.sqrt(eig_vals[i])
    arrow = Arrow3D(
        [mean[0], mean[0]+vec[0]],
        [mean[1], mean[1]+vec[1]],
        [mean[2], mean[2]+vec[2]],
        mutation_scale=20,
        lw=3,
        arrowstyle='-|>',
        color='r'
    )
    ax.add_artist(arrow)

plt.show()
