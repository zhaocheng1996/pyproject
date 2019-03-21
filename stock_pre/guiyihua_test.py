import pandas as pd
from sklearn.preprocessing import MinMaxScaler


f = open('dataset_2.csv')
df = pd.read_csv(f)
print(df.shape)


x_data = df.iloc[:,2:9].values #取第3-10列
#y_data = df.loc['lable'].values
y_data = df.iloc[:,9].values

scaler = MinMaxScaler()
min_max_x_data = scaler.fit(x_data)
min_max_y_data = scaler.fit(y_data)

print(x_data.shape)#(6109,7)
#print(x_data)
#print(y_data.shape)
print(y_data)


train_begin = 0
train_end = test_begin = 5800
train_x = min_max_x_data[train_begin:train_end]
print('train_x',train_x)
#print(train_x.shape)#(5800, 7)
test_x = x_data[train_end:]
#print(test_x.shape)#(309,7)
train_y = min_max_y_data[train_begin:train_end]
test_y = y_data[test_begin:]


print('train_x',train_x)
print('train_y',train_y)






