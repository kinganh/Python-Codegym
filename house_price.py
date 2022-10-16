from matplotlib import markers
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('Data\house_price_dống-da.xlsx')
df.info()

df1 = df[['area','price','toilet','bedroom','floor']]
df1.fillna(0,inplace=True)

sns.boxplot(df1['price'])
plt.show()

Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
df2 = df1[~((df1['price'] < (Q1  -1.5*IQR)) | (df1['price'] >  (Q3 + 1.5*IQR)))]
df2.info()

# Vẽ biểu đồ phân tích mối liên hệ giữa diện tích với giá nhà, giữa số phòng ngủ với giá nhà, giữa số toilet với giá nhà.
w = df2['price']
x = df2['area']
y = df2['bedroom']
z = df2['toilet']
plt.scatter(x,w)
plt.scatter(y,w)
plt.scatter(z,w)
plt.show()

df['type_of_land'] = df['type_of_land'].apply(lambda x: str(x).strip())
# Vẽ biểu đồ so sánh giá nhà trung bình trên 1m2 giữa các hình thức nhà (type_of_land).
df = df[df.area != 0]
tol = df.type_of_land.unique() # return a array
tol.sort()

df['gia/m2'] = df['price'] / df['area']
df.dropna(subset=['gia/m2'], inplace=True)
giatb = df.groupby('type_of_land')['gia/m2'].mean() # return a series (index auto-sorted)

plt.bar(tol,giatb)
plt.show()

# Vẽ biểu đồ thể hiện tỉ lệ % bài đăng (bản ghi) giữa các hình thức nhà (type_of_land).
records = df.groupby('type_of_land')['title'].count()
print(records)
plt.pie(records, labels=tol, autopct='%1.2f%%')
plt.show()

# Vẽ biểu đồ thể hiện sự thay đổi giá nhà trung bình trên 1m2 theo số lượng phòng ngủ.
df5 = df.dropna(subset='bedroom')
bedroom  = df5.bedroom.unique()
bedroom.sort()
gia = df5.groupby('bedroom')['gia/m2'].mean()
plt.plot(bedroom, gia, marker='o')
plt.show()