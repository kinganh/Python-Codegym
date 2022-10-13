import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder

df = pd.read_csv('Data\OnlineRetail.csv', encoding = 'ISO-8859-1')
print(df.shape)
df.info()

df.isna()

df = df[df['Quantity'] >= 0]

df1 = df.dropna()
print(df1.shape)
df1.info()

df2 = df.dropna(how='all') # xóa dòng khuyết thuyết hoàn toàn
df3 = df.dropna(thresh=7)  # xóa dòng có ít nhất 7 giá trị không khuyết thiếu
df4 = df.dropna(subset='CustomerID') # xóa dòng có giá trị khuyết thiếu ở cột CustomerID
df5 = df
df5['CustomerID'] = df5['CustomerID'].fillna(-1)
df5['Country'] = df5['Country'].fillna(method='ffill') #fronfill

##### Xử lý dữ liệu ngoại lại
sns.boxplot(x= df1['Quantity'])
plt.show()

Q1 = df1['Quantity'].quantile(0.25)
Q3 = df1['Quantity'].quantile(0.75)
IQR = Q3 - Q1

df1 = df1[~((df1['Quantity'] < (Q1 - 1.5*IQR)) | (df1['Quantity'] > (Q3 + 1.5*IQR)))]
sns.boxplot(x= df1['Quantity'])
plt.show()

##### Chuẩn hóa dữ liệu
standard = StandardScaler()
df_s1 = standard.fit_transform(df1[['Quantity']])
df_s1 = pd.DataFrame(df_s1)
df_s1.boxplot()
plt.show()
sns.kdeplot(data=df_s1)
plt.show()
print(df_s1)
MinMax = MinMaxScaler()
Robust = RobustScaler()

##### Mã hóa dữ liệu
OneHot = OneHotEncoder()
coded_data1 = OneHot.fit_transform(np.asarray(df1['Country']))
coded_data1.todense()
pd.get_dummies(df1['Country']) # mã hóa bằng Pandas

Label = LabelEncoder()
coded_data2 = Label.fit_transform(np.asarray(df1['Country']))
df1['Country'].astype('category').cat.codes # mã hóa bằng Pandas

##### Rời rạc hóa dữ liệu
cut = pd.cut(df['Quantity'], 5)
pd.value_counts(cut)
qcut= pd.qcut(df['Quantity'], 5)
pd.value_counts(qcut)