#!/usr/bin/env python
# coding=utf-8
# author: Tony

import csv
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# load data
x_data = []
y_data = []
x_datatime = []
with open('total_week.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        row = [float(i) for i in row]
        x_data.append(row[2:])
        y_data.append(row[1])
        x_datatime.append(row[0])

#print('x_datatime:',x_datatime)

row = np.shape(x_data)[0]
col = np.shape(x_data)[1]

# import data
train_start = 0
train_end = int(np.floor(0.8*row))
test_start = train_end + 1
test_end = row
x_train = x_data[train_start:train_end]
y_train = y_data[train_start:train_end]
x_test = x_data[test_start:test_end]
y_test = y_data[test_start:test_end]

#x_datatime_test = x_datatime[test_start:test_end]
#print(x_datatime_test)
#datatimestr=str(x_datatime_test)
#print(type(datatimestr))

x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)


model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print('常数项：',model.intercept_)
print('多项式参数：',model.coef_)#
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
sum=sum(y_test)
average=sum/len(y_test)
loss_rate=mse/average
print('loss_rate',loss_rate)
print('直接模型mse',mse)

# deduce=abs(y_test-y_pred)
# new_deduce=np.round(deduce,2)
# print(new_deduce)
# error=np.round(deduce/y_test,4)
# print("error:",error)

# average_error=sum(error)/len(y_test)
# print(average_error)
# print("average_error",'%.4f%%' % (average_error*100))

#交叉验证
from sklearn.model_selection import cross_val_predict
pre=cross_val_predict(model,x_test,y_test,cv=10)
#print(pre.shape,y_test.shape)
mse=mean_squared_error(y_test,pre)
print('交叉验证mse：',mse)

fig=plt.figure()
#’b'指的是蓝色，‘r’指的是红色
plt.plot(range(len(y_pred)),y_pred,'b',label='predict')
plt.plot(range(len(y_pred)),y_test,'r',label='test')
plt.xlabel('week')
plt.ylabel('priceindex')
#my_x_ticks = np.arange(201704, 201748, 1)
#plt.xticks(my_x_ticks)
#ax=fig.add_subplot(1,1,1)
#label = ax.set_xticklabels(datatimestr)
plt.legend(loc='upper right')#加标签右上
plt.show()
