
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

f = open('dataset_2.csv')
df = pd.read_csv(f)
print(df.shape)
x_data = df.iloc[:,2:9].values #取第3-10列
#y_data = df.loc['lable'].values
y_data = df.iloc[:,9].values

print(x_data.shape)#(6109,7)
#print(x_data)
#print(y_data.shape)
print(y_data)


train_begin = 0
train_end = test_begin = 5800
train_x = x_data[train_begin:train_end]
print('train_x',train_x)
#print(train_x.shape)#(5800, 7)
test_x = x_data[train_end:]
#print(test_x.shape)#(309,7)
train_y = y_data[train_begin:train_end]
test_y = y_data[test_begin:]


model = LinearRegression()
model.fit(train_x, train_y)
pred_y = model.predict(test_x)

print('常数项：',model.intercept_)
print('多项式参数：',model.coef_)#

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(test_y, pred_y)
#print(y_test.shape,y_pred.shape)
print('直接模型mse',mse)
acc = np.average(np.abs(pred_y - test_y[:len(pred_y)]) / test_y[:len(pred_y)])  # 偏差程度
print("The accuracy of this predict:", acc)


plt.figure()
#’b'指的是蓝色，‘r’指的是红色
plt.plot(range(len(pred_y)),pred_y,'b',label='predict')
plt.plot(range(len(pred_y)),test_y,'r',label='test')
plt.xlabel('date')
plt.ylabel('price')
plt.legend(loc='upper right')#加标签右上
plt.show()





