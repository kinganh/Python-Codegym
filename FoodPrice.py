import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder
import scipy as sp

df = pd.read_csv('Data\FoodPrice_in_Turkey.csv', encoding='ISO-8859-1')

df.info()
print(df.describe())

df.isna()
df1 = df.dropna()
print(df1.shape)

sns.boxplot(x=df['Price'])
plt.show()

# Loại bỏ Outliers
Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3-Q1
df2 = df[~((df['Price'] < (Q1 - 1.5*IQR)) | (df['Price'] > (Q3 + 1.5*IQR)))]
print(df2.shape)

sns.boxplot(x=df2['Price'])
plt.show()
sns.kdeplot(data=df2['Price'])
plt.show()

##### Chuẩn hóa dữ liệu
scaler1 = StandardScaler()
df_s1 = scaler1.fit_transform(df2[['Price']])
df_s1 = pd.DataFrame(df_s1)
df_s1.boxplot()
plt.show()
sns.kdeplot(data=df_s1)
plt.show()

scaler2 = MinMaxScaler()
df_s2 = scaler2.fit_transform(df2[['Price']])
df_s2 = pd.DataFrame(df_s2)
df_s2.boxplot()
plt.show()
sns.kdeplot(data=df_s2)
plt.show()

scaler3 = RobustScaler()
df_s3 = scaler3.fit_transform(df2[['Price']])
df_s3 = pd.DataFrame(df_s3)
df_s3.boxplot()
plt.show()
sns.kdeplot(data=df_s3)
plt.show()

##### Mã hóa dữ liệu cột #ProductName
df2['ProductName'].unique()

one = OneHotEncoder() # OneHot bằng Scikitlearn
encoded_data1 = one.fit_transform(np.asarray(df2['ProductName']).reshape(-1,1))
encoded_data1.todense() # return a maxtrix
print(encoded_data1)
pd.get_dummies(df2['ProductName']) # OneHot bằng Pandas

lab = LabelEncoder() # Label bằng Scikitlearn
encoded_data2 = lab.fit_transform(np.asarray(df2['ProductName']))
print(encoded_data2)
df2['ProductName'].astype('category').cat.codes # Label bằng Pandas

##### Rời rạc hóa dữ liệu
cats = pd.cut(df2['Price'], 5)
print(pd.value_counts(cats))

catss = pd.qcut(df2['Price'], 5)
print(pd.value_counts(catss))



