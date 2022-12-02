import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv('Data\ApartmentTrading.csv', encoding = 'UTF-8')

# Preprocessing: dien_tich, huong_ban_cong, phong_ngu, noi_that, huong_nha, lat, long, du_an, id_duong, id_phuong, %gia_m2
df['ten_quan'] = df['ten_quan'].replace('Quận Hà Đông', 'Hà Đông') # đồng nhất tên quận
df = df[df['ten_quan'] == 'Hà Đông'] #filter df theo quận
df = df[df['dien_tich'].notnull()].reset_index() # 97.66% notnull

phong_ngu = []
cache = df['phong_ngu'].tolist()
for i in cache:
    if pd.isna(i):
        phong_ngu.append(df['dien_tich'][cache.index(i)]//40 + 1)
    else:
        phong_ngu.append(i)
df['phong_ngu_new'] = phong_ngu

# chọn features
df = df[['dien_tich', 'huong_ban_cong', 'phong_ngu_new', 'noi_that', 'huong_nha', 'lat', 'long', 'du_an', 'id_duong', 'id_phuong', 'gia_m2']]

sns.boxplot(x=df['dien_tich'])
plt.show()
sns.boxplot(x=df['phong_ngu_new'])
plt.show()
sns.boxplot(x=df['gia_m2'])
plt.show()

# loại bỏ ngoại lai, dùng cột dien_tich làm tham chiếu
Q1 = df['dien_tich'].quantile(0.25)
Q3 = df['dien_tich'].quantile(0.75)
IQR = Q3 - Q1
df1 = df[~((df['dien_tich'] < (Q1 - 1.5*IQR) ) | (df['dien_tich'] > (Q3 + 1.5*IQR)))]

# loại bỏ ngoại lai, dùng cột phong_ngu_new làm tham chiếu
Q1_ = df1['phong_ngu_new'].quantile(0.25)
Q3_ = df1['phong_ngu_new'].quantile(0.75)
IQR = Q3_ - Q1_
df2 = df1[~((df1['phong_ngu_new'] < (Q1_ - 1.5*IQR) ) | (df1['phong_ngu_new'] > (Q3_ + 1.5*IQR)))]

# loại bỏ ngoại lai, dùng cột gia_m2 làm tham chiếu
Q1_1 = df2['gia_m2'].quantile(0.25)
Q3_1 = df2['gia_m2'].quantile(0.75)
IQR = Q3_1 - Q1_1
df3 = df2[~((df2['gia_m2'] < (Q1_1- 1.5*IQR) ) | (df2['gia_m2'] > (Q3_1 + 1.5*IQR)))]

# fill dữ liệu khuyết thiếu
df3['huong_nha'] = df3['huong_nha'].str.replace('-', ' ').fillna('KXĐ').astype('category').cat.codes
df3['huong_ban_cong'] = df3['huong_ban_cong'].str.replace('-', ' ').fillna('KXĐ').astype('category').cat.codes
df3['du_an'] = df3['du_an'].fillna('unknown').astype('category').cat.codes
df3['id_duong'] = df3['id_duong'].fillna('unknown').astype('category').cat.codes
df3['id_phuong'] = df3['id_phuong'].fillna('unknown').astype('category').cat.codes
df3['gia_m2'] = df3['gia_m2'].fillna(df3['gia_m2'].median())
df3['noi_that'] = df3['noi_that'].fillna('Nội thất cơ bản')

def convert_furniture(furniture):
    try:
        furniture = furniture.lower()
        if _found_text(furniture, ['kéo vali', 'xách vali', 'mang vali', 'ở ngay', 'full đồ', 'mang quần áo vào ở', 'đủ đồ']):
            return 2
        elif _found_text(furniture, ['cơ bản', 'nguyên bản', 'đã có đồ']):
            return 1
        elif (_found_text(furniture, ['điều hoà', 'tủ bếp'])):
            if _found_text(furniture, ['giường']):
                return 2
            elif _found_text(furniture, ['thiếu', 'giường']):
                return 1
            else:
                return 1
        elif _found_text(furniture, ['nội thất']):
            if _found_text(furniture, ['cao cấp', 'đầy đủ', 'full']):
                return 2
            elif _found_text(furniture, ['cơ bản']):
                return 1
        elif _found_text(furniture, ['đầy đủ nội thất cơ bản']):
            return 1
    except:
        return 0
def _found_text(text, list_item):
    for item in list_item:
        if item in text:
            return True
    return False

furniture = []
cache = df3['noi_that'].tolist()
for i in cache:
    k = convert_furniture(i)
    furniture.append(k)
print(furniture)
df3['furniture'] = furniture

# Xây dựng mô hình
X, y = df3.drop(columns=['noi_that','gia_m2']), df3['gia_m2']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

# Đánh giá mô hình
print('R-squared: ', r2_score(y_test, y_pred))
print('MAPE:', mean_absolute_percentage_error(y_test, y_pred))