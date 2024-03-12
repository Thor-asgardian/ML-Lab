import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\pc\\Desktop\\pholdur\\ToyotaCorolla.csv")

x = data['km']
y = data['price']
z = data['weight']

plt.scatter(x, y, c=z, cmap='summer', edgecolor='black', linewidths=1, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Weight')
plt.title("Price of Toyota Corolla")
plt.xlabel('KM')
plt.ylabel('Price')
plt.show()
