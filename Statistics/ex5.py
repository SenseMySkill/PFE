import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

data_flat = np.genfromtxt("PCAdata.txt")
data = data_flat.reshape(-1, 3)

mean = np.mean(data, axis=0)
data_centered = data - mean

cov_matrix = np.cov(data_centered, rowvar=False)

eig_vals, eig_vecs = np.linalg.eig(cov_matrix)

idx = np.argsort(eig_vals)[::-1]
eig_vecs = eig_vecs[:, idx]
eig_vals = eig_vals[idx]

top2_vecs = eig_vecs[:, :2]

data_2D = data_centered @ top2_vecs

plt.figure(figsize=(7,6))
plt.scatter(data_2D[:,0], data_2D[:,1], c='blue', s=50)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.grid(True)
plt.show()


pca = PCA(n_components=2)
data_2D_sklearn = pca.fit_transform(data)

plt.figure(figsize=(7,6))
plt.scatter(data_2D_sklearn[:,0], data_2D_sklearn[:,1], c='red', s=50)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.grid(True)
plt.show()

print("Manual PCA 2D shape:", data_2D.shape)
print("Sklearn PCA 2D shape:", data_2D_sklearn.shape)




explained_variance_ratio = eig_vals / np.sum(eig_vals)
cumulative_variance = np.cumsum(explained_variance_ratio)
num_pc_90 = np.argmax(cumulative_variance >= 0.90) + 1
print(num_pc_90)