import pandas as pd
import numpy as np


f = open('dataset_2.csv')
df = pd.read_csv(f)
data = df.iloc[:,2:10].values #取第3-10列


#获取训练集
def get_train_data(batch_size=60,time_step=20,train_begin=0,train_end=5800):
    batch_index=[];
    data_train=data[train_begin:train_end]
    normalized_train_data=(data_train-np.mean(data_train,axis=0))/np.std(data_train,axis=0)#标准化
    train_x,train_y=[],[]
    for i in range(len(normalized_train_data)-time_step):
#    for i in range(len(data_train) - time_step):#5800-20
        if i % batch_size==0:
            batch_index.append(i)
        x = normalized_train_data[i:i + time_step, :7]
        #x = data_train[i:i + time_step, :7]#一维的1到20(行），二维的7(列)
        y=normalized_train_data[i:i+time_step,7,np.newaxis]
        #y = data_train[i:i + time_step, 7, np.newaxis]#np.newaxis为多维数组增加一个轴
        train_x.append(x.tolist())#x.tolist将数组或矩阵转为列表list是长第一个位置是一个20*7的矩阵，第二个位置也是20*7的矩阵，一共有5800-20个
        train_y.append(y.tolist())
    batch_index.append((len(normalized_train_data)-time_step))
    #batch_index.append((len(data_train)-time_step))
    return batch_index,train_x,train_y


batch_index,train_x,train_y = get_train_data()
# print(batch_index[:10])
#print('train_x',train_x[:10])#train_x的维度是(5780, 20, 7)
# print('train_y',train_y[:10])

#获取测试集
def get_test_data(time_step=20,test_begin=5800):
    data_test=data[test_begin:]
    mean=np.mean(data_test,axis=0)
    std=np.std(data_test,axis=0)
    normalized_test_data=(data_test-mean)/std  #标准化
    size=(len(normalized_test_data)+time_step-1)//time_step  #有size个sample
    test_x,test_y=[],[]
    for i in range(size-1):
       x=normalized_test_data[i*time_step:(i+1)*time_step,:7]
       y=normalized_test_data[i*time_step:(i+1)*time_step,7]
       test_x.append(x.tolist())#append
       test_y.extend(y)#使用a.extend(b)后，可以得到一个包含a和b所有元素的列表。
    test_x.append((normalized_test_data[(i+1)*time_step:,:7]).tolist())
    test_y.extend((normalized_test_data[(i+1)*time_step:,7]).tolist())
    return mean,std,test_x,test_y

# mean,std,test_x,test_y = get_test_data(time_step=20,test_begin=5800)
# print(len(test_y))#309


