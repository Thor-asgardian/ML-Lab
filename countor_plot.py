import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("C:\\Users\\pc\\Desktop\\pholdur\\ToyotaCorolla.csv")

x = data['km']
y = data['weight']
z = data['price']

plt.tricontourf(x, y, z, levels=20, cmap='jet')
plt.colorbar(label='Price')
plt.xlabel('Kilometers')
plt.ylabel('Weight')
plt.title('Contour Plot')
plt.show()
