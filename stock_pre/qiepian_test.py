import pandas as pd
import numpy as np

f = open('dataset_2.csv')
df = pd.read_csv(f)
data = df.iloc[:,2:10].values #取第3-10列
time_step = 20
data_train = data[0:5800]
print(data_train.shape)
#print(data_train)

x = data_train[0:0+ time_step, :7]#一维的1到20(行），二维的7(列)
print('X:',x)
print(x.shape)


