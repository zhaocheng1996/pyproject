
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

f = open('dataset_2.csv')
df = pd.read_csv(f)
print(df.shape)
x_data = df.iloc[:,2:9].values #取第3-10列
#y_data = df.loc['lable'].values
y_data = df.iloc[:,9].values


train_begin = 0
train_end = test_begin = 5800

train_x = x_data[train_begin:train_end]
#print('标准化前的：',train_x)
#print(train_x.shape)#(5800, 7)
test_x = x_data[train_end:]
#print(test_x.shape)#(309,7)
train_y = y_data[train_begin:train_end]
print('train_y:',train_y.shape)
test_y = y_data[test_begin:]
#print(test_x)

ss_x = StandardScaler()
ss_y = StandardScaler()
train_x = ss_x.fit_transform(train_x)

test_x = ss_x.fit_transform(test_x)
train_y = train_y.reshape(-1,1)
print('train_y:',train_y.shape)
train_y = ss_y.fit_transform((train_y))
test_y = test_y.reshape(-1,1)
test_y = ss_y.fit_transform(test_y)
print('标准化：',train_x)
print('标准化后的test：',test_x)

#svr_rbf = SVR(kernel='rbf', C=0.2)#径向基函数（RBF
svr_lin = SVR(kernel='linear', C=10)
#svr_poly = SVR(kernel='poly', C=1, degree=2)

# svr_rbf.fit(train_x,train_y)
# pred_y = svr_rbf.predict(test_x)
#print('pred_y:',pred_y)

svr_lin.fit(train_x,train_y)
pred_y = svr_lin.predict(test_x)

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

