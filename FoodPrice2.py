import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data\FoodPrice_in_Turkey.csv', encoding='ISO-8859-1')

# Vẽ các biểu đồ cột so sánh giá Milk (powder, infant formula) và Fuel (gas) tháng 12 năm 2019 
# của Ankara, Istanbul, Izmir và National Average.
d11 = df[(df['Year'] == 2019) & (df['Month'] == 12) & (df['ProductName'] == 'Milk (powder, infant formula) - Retail')].reset_index()
d12 = df[(df['Year'] == 2019) & (df['Month'] == 12) & (df['ProductName'] == 'Fuel (gas) - Retail')].reset_index()
df1 = pd.DataFrame({'x': d11['Place'], 'y1': d11['Price'], 'y2': d12['Price']})

df1.plot(x = 'x', y = ['y1', 'y2'], kind = 'bar')
plt.title('Milk and Gas Price in 12/2019', fontsize = 16, color = 'r')
plt.xlabel('Place', fontsize = 14)
plt.ylabel('Price', fontsize = 14)
plt.show()

# Vẽ các biểu đồ đường phân tích xu hướng giá gạo (Rice-Retail), giá Fuel (gas) trung bình cả nước (National Average) 
# trong năm 2016, 2018, 2019 tại Thổ Nhĩ Kì.
# Vẽ biểu đồ Scatter phân tích mối liên quan giữa giá gạo và giá gas trung bình quốc gia (National Average) 
# tại Thổ Nhĩ Kì các năm 2016, 2018, 2019.
d21 = df[(df['Place'] == 'National Average') & (df['Year'] == 2016) & (df['ProductName'] == 'Milk (powder, infant formula) - Retail')]
d22 = df[(df['Place'] == 'National Average') & (df['Year'] == 2016) & (df['ProductName'] == 'Fuel (gas) - Retail')]
d23 = df[(df['Place'] == 'National Average') & (df['Year'] == 2018) & (df['ProductName'] == 'Milk (powder, infant formula) - Retail')]
d24 = df[(df['Place'] == 'National Average') & (df['Year'] == 2018) & (df['ProductName'] == 'Fuel (gas) - Retail')]
d25 = df[(df['Place'] == 'National Average') & (df['Year'] == 2019) & (df['ProductName'] == 'Milk (powder, infant formula) - Retail')]
d26 = df[(df['Place'] == 'National Average') & (df['Year'] == 2019) & (df['ProductName'] == 'Fuel (gas) - Retail')]

d31 = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Fuel (gas) - Retail') & (df['Year'] == 2016)]
d32 = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Milk (powder, infant formula) - Retail') & (df['Year'] == 2016)]
d33 = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Fuel (gas) - Retail') & (df['Year'] == 2018)]
d34 = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Milk (powder, infant formula) - Retail') & (df['Year'] == 2018)]
d35 = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Fuel (gas) - Retail') & (df['Year'] == 2019)]
d36 = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Milk (powder, infant formula) - Retail') & (df['Year'] == 2019)]

fig, ax = plt.subplots(3, 2)
ax[0][0].plot(d21['Month'], d21['Price'], marker = '*', label = 'Milk-2016')
ax[0][0].plot(d22['Month'], d22['Price'], marker = 's', label = 'Gas-2016')
ax[0][0].set_ylabel('Price')
ax[0][0].set_xticklabels([])
ax[0][0].set_title('2016')

ax[1][0].plot(d23['Month'], d23['Price'], marker = '*', label = 'Milk-2018')
ax[1][0].plot(d24['Month'], d24['Price'], marker = 's', label = 'Gas-2018')
ax[1][0].set_ylabel('Price')
ax[1][0].set_xticklabels([])
ax[1][0].set_title('2018')

ax[2][0].plot(d25['Month'], d25['Price'], marker = '*', label = 'Milk')
ax[2][0].plot(d26['Month'], d26['Price'], marker = 's', label = 'Gas')
ax[2][0].set_ylabel('Price')
ax[2][0].set_xlabel('Month')
ax[2][0].legend()
ax[2][0].set_title('2019')

ax[0][1].scatter(d31['Price'], d32['Price'])
ax[0][1].set_title('2016')
ax[0][1].set_ylabel('Rice')
ax[0][1].set_xticklabels([])

ax[1][1].scatter(d33['Month'], d34['Price'])
ax[1][1].set_title('2018')
ax[1][1].set_xticklabels([])

ax[2][1].scatter(d35['Month'], d36['Price'])
ax[2][1].set_title('2019')
ax[2][1].set_xlabel('Gas')
plt.show()