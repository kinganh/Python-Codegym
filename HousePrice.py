from optparse import Values
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

df = pd.read_excel('Data\house_price_dống-da.xlsx')

# Phát hiện các dòng, cột chứa dữ liệu khuyết thiếu
# Xóa bỏ hết tất cả những dòng dữ liệu không có thông tin về giá
# Thực hiện xử lý giá trị khuyết thiếu: Thay thế giá trị khuyết thiếu của land_certificate bằng =”không có thông tin”,
# house_direction, balcony_direction, toilet, bedroom, Floor bằng giá trị có tần số xuất hiện lớn nhất của các thuộc tính đó,
# Lọc thông tin những bất động sản ở trong ngõ thành bộ dữ liệu nhà ngõ
# Tính toán giá/m2  ( đơn vị triệu/m2) với loại hình nhà ngõ
# Phát hiện giá trị ngoại lai của các thuộc tính: diện tích, giá/m2 bằng phương pháp IQR
# Thực hiện loại bỏ các dòng dữ liệu ngoại lai
# Chuẩn hóa dữ liệu của tất cả các thuộc tính: price/m2 bằng các phương pháp: min-max scaling, z- score scaling, Robust scaling
# và so sánh phân bố của thuộc tính này trước và sau khi chuẩn hóa

# df.info()
df.isna()
df.dropna(subset='price', inplace=True)

print(df.house_direction.mode())

df['land_certificate'] = df['land_certificate'].fillna('không có thông tin')
df['house_direction'] = df['house_direction'].fillna(df.house_direction.mode())
# df['balcony_direction'] = df['balcony_direction'].fillna(df.balcony_direction.mode().values)
# df['toilet'] = df['toilet'].fillna(df.toilet.mode().values)
# df['bedroom'] = df['bedroom'].fillna(df.bedroom.mode().values)
# df['floor'] = df['floor'].fillna(df.floor.mode().values)

df.info()



# df.to_excel('varwefa.xlsx')
