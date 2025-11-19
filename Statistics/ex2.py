import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

#=========1=========

x = np.random.normal(1.0, 1.0, 1000)
y = np.random.normal(1.0, 1.0, 1000)

plt.scatter(x, y, alpha=0.5)
plt.show()

#=========2=========

scal_mtx = np.array([[3, 0],
                     [0, 1]])

points = np.vstack((x, y))

points_new = scal_mtx @ points

x_new = points_new[0, :]
y_new = points_new[1, :]

plt.scatter(x_new, y_new, alpha=0.5)
plt.show()

#=========3=========
theta = np.pi / 4
rot_mtx = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta),  np.cos(theta)]])

points_new2 = rot_mtx @ points

x_new2 = points_new2[0, :]
y_new2 = points_new2[1, :]

plt.scatter(x_new2, y_new2, alpha=0.5)
plt.show()

#=========4=========

# poprzez pomnożenie scal @ rot @ points
points_new3 = scal_mtx @ rot_mtx @ points

#=========5=========
print("\n=========5=========\n")

x_new3 = points_new3[0, :]
y_new3 = points_new3[1, :]

corr_matrix = np.corrcoef(x_new3, y_new3)
corr = corr_matrix[0, 1]

print(corr)

#=========6=========
print("\n=========6=========\n")

cov_matrix = np.cov(points_new3)
print(cov_matrix)

eigvals, eigvecs = np.linalg.eig(cov_matrix)

print(eigvals, eigvecs)

Lambda_inv_sqrt = np.diag(1.0 / np.sqrt(eigvals))

T_inv = eigvecs @ Lambda_inv_sqrt @ eigvecs.T

mean_vec = np.mean(points_new3, axis=1, keepdims=True)

points_whitened = T_inv @ (points_new3 - mean_vec)

x_wh = points_whitened[0, :]
y_wh = points_whitened[1, :]

plt.scatter(x_wh, y_wh, alpha=0.5)
plt.show()
