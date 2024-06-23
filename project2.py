                         # CARS DATA PREDICTION
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



cars_data=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Desktop\\placement pqp\\Toyota.csv",index_col=0,na_values=['??','????'])
cars_data1 = cars_data.copy()
cars_data2 = cars_data.copy()

datas = cars_data.info()

missing_values = cars_data1.isnull().sum()

data = cars_data1.describe()


cars_data1['Age'].fillna(cars_data['Age'].mean(),inplace=True)



#cars_data1['KM'].astype('int64')
#new=cars_data1
#print(new)


cars_data1['KM'].fillna(cars_data1['KM'].median(),inplace=True)



cars_data1['FuelType'].fillna(cars_data1['FuelType'].value_counts().index[0],inplace=True)




cars_data1['MetColor'].fillna(cars_data1['MetColor'].mode().index[0],inplace=True)


cars_data1['HP'].fillna(cars_data['HP'].mean(),inplace=True)

#print(cars_data1.isnull().sum())

missing_values = cars_data1.isnull().sum()
print(missing_values)

plt.scatter(cars_data1['Age'],cars_data1['Price'])

plt.title("Relation ship between age price of the cars")

plt.xlabel("Age")

plt.ylabel("Price")

plt.show()

plt.scatter(cars_data1['KM'],cars_data1['Price'])

plt.title("Relation ship between KM, price of the cars")

plt.xlabel("KM")

plt.ylabel("Price")

plt.show()

rela=pd.crosstab(index=cars_data1['Price'],columns='count',dropna=True)
#print(cars_data1.info())

plt.hist(cars_data1['KM'],color='green',edgecolor='white',bins=5)
plt.title('Relationship between KM using Histogram')

plt.xlabel('Km')
plt.ylabel('Frequency')
plt.show()

#print(cars_data1.info())
w=('petrol','Diesel','cng')
#Fueltype=np.unique(cars_data1['FuelType'])
counts=cars_data1['FuelType'].value_counts()
t=len(counts)

plt.bar(counts.index,counts, color=['green','blue','red'])
plt.title('Relation ship between Fueltype vechiles')

plt.xlabel('fueltype')
plt.ylabel('vechile counts')
plt.xticks(w.index)
plt.show()

#print(cars_data1.corr())


