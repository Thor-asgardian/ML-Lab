import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv("C:\\Users\\pc\\Desktop\\pholdur\\ToyotaCorolla.csv")

x = data['km']
y = data['doors']
z = data['price']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(x, y, z, cmap='jet')
ax.set_title("3D surface plot")
ax.set_xlabel('Kilometers')
ax.set_ylabel('Doors')
ax.set_zlabel('Price')

plt.show()
