import csv
import numpy
import matplotlib.pyplot as plt
import pandas as pd

housing_Data = pd.read_csv('train.csv', sep=",")
#print housing_Data.columns
#print housing_Data['SalePrice'].describe()

var = 'OverallQual'
data = pd.concat([housing_Data['SalePrice'], housing_Data[var]], axis=1)
data.plot.scatter(x=var, y='SalePrice', ylim=(0,800000));
plt.show()
print("done")