# Heat maps
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:\\Users\\pc\\Desktop\\pholdur\\ToyotaCorolla.csv")

# x = data['km']
# y = data['price']
# z = data['weight']

# plt.scatter(x, y, c=z, cmap='summer', edgecolor='black', linewidths=1, alpha=0.75)
plt.boxplot([data["price"], data["hp"], data["km"]])

plt.xticks([1,2,3], ["price", "hp", "km"])

plt.show()
