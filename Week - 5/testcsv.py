import pandas as pd
import matplotlib.pyplot as plt

path_to_csv= "/Users/nbvenkatesh88/Desktop/heatmapValuesSet1.csv"
df = pd.read_excel(path_to_csv ,index_col=0)
plt.imshow(df,cmap='hot',interpolation='nearest')
plt.show()