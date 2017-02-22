import csv
import numpy
from sklearn import datasets, linear_model
import pandas
from statsmodels.formula.api import ols
data = pandas.read_csv('project/train.csv',sep=',')


#subseting example
#t = data[data['YrSold']==2009] 
model = ols("SalePrice ~ LotArea",data).fit()
print(model.summary())
print("done")

