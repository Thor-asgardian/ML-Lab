# Heat maps
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:\\Users\\pc\\Desktop\\pholdur\\ToyotaCorolla.csv")

# x = data['km']
# y = data['price']
# z = data['weight']

# Extracting correlation matrix
corr_matrix = data[["price", "km", "doors", "weight"]].corr()

# Plotting heatmap
sns.heatmap(corr_matrix, cmap='jet', annot=True)

plt.show()
