import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder

df = pd.read_csv('Data\Credit_Scoring.csv')

# Nêu thông tin về kiểu dữ liệu và khoảng dữ liệu ở các cột
# Kiểm tra dữ liệu khuyết thiếu
# Thực hiện xử lý giá trị khuyết thiếu: Thay thế giá trị khuyết thiếu bằng giá trị nội suy theo các cột
# Thực hiện xử lý giá trị khuyết thiếu: Thay thế giá trị khuyết thiếu bằng giá trị 0
# Vẽ biểu đồ boxplot, biểu đồ phân bố dữ liệu cho các cột
# Loại bỏ giá trị ngoại lai
# Chia dữ liệu ở các cột thành 4,5,6 nhóm có số lượng phần tử bằng nhau và đếm số lượng phần tử ở mỗi nhóm, lấy ra khoảng giữ liệu của mỗi nhóm.
# Chia dữ liệu ở các cột age và MonthlyIncome thành 5 nhóm theo các khoảng: 0, 30, 40, 50, 80, 150 và đếm số lượng phần tử ở mỗi nhóm.
# Đặt tên bất kỳ cho các nhóm ở 2 ý trên.

df.info()
del df['Unnamed: 0']

df.isna()
df1 = df.interpolate(axis=1) # thay thế dữ liệu khuyết thiếu bởi giá trị nội suy theo cột
df2 = df.fillna(0)

# df2.boxplot()
# plt.show()
# sns.kdeplot(data=df2[['NumberOfTimes90DaysLate','NumberOfTime60-89DaysPastDueNotWorse','NumberOfDependents']])
# plt.show()

Q1 = df2.quantile(0.25)
Q3 = df2.quantile(0.75)
IQR = Q3 - Q1

df3 = df2[~((df < (Q1 - 1.5*IQR) ) | (df > (Q3 + 1.5*IQR)))]

# df3.boxplot()
# plt.show()
# sns.kdeplot(data=df3)
# plt.show()

bins = [0, 30, 40, 50, 80, 150]
cut = pd.cut(df3['age'], bins)
print(pd.value_counts(cut))

group_name = ['Giang', 'Kien', 'Nhi', 'Heo']
qcut = pd.qcut(df3['MonthlyIncome'], 7, labels=group_name, duplicates='drop')
print(pd.value_counts(qcut))

# print(qcut)
# print(qcut.codes)
# print(qcut.categories)