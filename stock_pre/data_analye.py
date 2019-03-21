import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
#处理时序数据
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y/%m/%d')
#---其中parse_dates 表明选择数据中的哪个column作为date-time信息，
#---index_col 告诉pandas以哪个column作为 index
#--- date_parser 使用一个function(本文用lambda表达式代替)，使一个string转换为一个datetime变量

data = pd.read_csv('dataset_2.csv',parse_dates=['date'],index_col='date',date_parser=dateparse)
# print(data.head())
# print(data.index)
ss_x = StandardScaler()

data_label = data['label']
data_close = data['close']
data_low = data['low']
#print('data_label',data_label)

data_label = data_label.reshape(-1,1)
data_low = data_low.reshape(-1,1)
data_label = ss_x.fit_transform(data_label)
data_low = ss_x.fit_transform(data_low)

#判断时间序列是否稳定
plt.figure()
plt.plot(data_label,color='blue',label='lable')
#plt.plot(data_close,color='red',label='close')
plt.plot(data_low,color='g',label='low')
plt.xlabel('date')
plt.ylabel('price')
plt.legend(loc='upper right')#加标签右上
plt.title('data_analye')
plt.show()