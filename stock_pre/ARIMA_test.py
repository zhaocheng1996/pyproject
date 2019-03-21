import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

#处理时序数据
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y/%m/%d')
#---其中parse_dates 表明选择数据中的哪个column作为date-time信息，
#---index_col 告诉pandas以哪个column作为 index
#--- date_parser 使用一个function(本文用lambda表达式代替)，使一个string转换为一个datetime变量

data = pd.read_csv('dataset_2.csv',parse_dates=['date'],index_col='date',date_parser=dateparse)
# print(data.head())
# print(data.index)

data_label = data['label']
print('data_label',data_label)


#判断时间序列是否稳定
plt.figure()
plt.plot(data_label,color='b',label='Original')
plt.xlabel('date')
plt.ylabel('price')
plt.legend(loc='upper right')#加标签右上
plt.show()

from statsmodels.tsa.stattools import adfuller
def test_stationarity(timeseries):
    # 这里以100天为一个窗口，每一个时间t的值由它前面100天（包括自己）的均值代替，标准差同理。
    rolmean = pd.rolling_mean(timeseries, window=200)
    rolstd = pd.rolling_std(timeseries, window=200)

    # plot rolling statistics:
    fig = plt.figure()
    fig.add_subplot()
    orig = plt.plot(timeseries, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='rolling mean')
    std = plt.plot(rolstd, color='black', label='Rolling standard deviation')

    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()

    # Dickey-Fuller test:

    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    # dftest的输出前一项依次为检测值，p值，滞后数，使用的观测数，各个置信度下的临界值
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical value (%s)' % key] = value

    print(dfoutput)

test_stationarity(data_label)



#处理时间序列：
#让时序数据变得稳定，去除趋势：平滑： 以一个滑动窗口内的均值代替原来的值，为了使值之间的差距缩小
#而在许多情况下，可以认为越近的时刻越重要。所以引入指数加权移动平均--
# Exponentially-weighted moving average.（pandas中通过ewma()函数提供了此功能。）
data_label_log = np.log(data_label)
# halflife的值决定了衰减因子alpha：  alpha = 1 - exp(log(0.5) / halflife)
expmoving_avg = pd.ewma(data_label_log,200)
data_label_log_moving_diff = data_label_log-expmoving_avg

print('aaaaaa')
print('data_label_log_moving_diff.type',data_label_log_moving_diff.dtype)

print('data_label_log_moving_diff:',data_label_log_moving_diff)
data_label_log_moving_diff.dropna(inplace = True)
test_stationarity(data_label_log_moving_diff)

#第四步 对时序数据进行预测
#一阶差分后数据已经稳定，所以d=1。所以用一阶差分化的data_label_log_moving_diff = data_label_log-expmoving_avg 作为输入
#先画出ACF,PACF的图像
from statsmodels.tsa.stattools import acf, pacf
#from statsmodels.graphics.tsaplots import acf, pacf
lag_acf = acf(data_label_log_moving_diff, nlags=20)
lag_pacf = pacf(data_label_log_moving_diff, nlags=20, method='ols')
#Plot ACF:
plt.subplot(121)
plt.plot(lag_acf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(data_label_log_moving_diff)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(data_label_log_moving_diff)),linestyle='--',color='gray')
plt.title('Autocorrelation Function')

#Plot PACF:
plt.subplot(122)
plt.plot(lag_pacf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(data_label_log_moving_diff)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(data_label_log_moving_diff)),linestyle='--',color='gray')
plt.title('Partial Autocorrelation Function')
plt.tight_layout()
plt.show()
#上下两条灰线之间是置信区间，p的值就是ACF第一次穿过上置信区间时的横轴值。
# q的值就是PACF第一次穿过上置信区间的横轴值。所以从图中可以得到p=0，q=2。

#通过ACF,PACF进行ARIMA（p，d，q）的p，q参数估计
from statsmodels.tsa.arima_model import ARIMA
model = ARIMA(data_label_log_moving_diff, order=(0, 1, 2))
results_AR = model.fit(disp=-1)
#print('results_AR.fittedvalues',results_AR.fittedvalues)
results_AR_values = results_AR.fittedvalues
print('results_AR_values',results_AR_values)#从1990-12-21开始
print('results_AR_values.shape',results_AR_values.shape)#(6108,)
#print('results_AR_values.dype',results_AR_values.dtype)
# pre_ = model.predict(data_label_log_moving_diff)
# print('pre',pre_)
# print('pre.shape:',pre_.shape)
# print('data_label.shape',data_label_log_moving_diff.shape)
plt.plot(data_label_log_moving_diff,color='b')
# print('data_label_log_moving_diff',data_label_log_moving_diff)#从1990-12-20   0.00开始
# print('data_label_log_moving_diff.shape',data_label_log_moving_diff.shape)
plt.plot(results_AR_values[1:], color='red')

#print('results_AR_values_array',results_AR_values_array)
# print('eee_notnull',eee[1:])
# print('bbbbbbbb')
eee = results_AR_values-data_label_log_moving_diff
# print('eee',eee)
# print('eeeend')
print('RSS: %.4f'% sum((eee[1:])**2))#RSS: 494.4760
plt.title('RSS: %.4f'% sum((eee[1:])**2))
plt.show()

# 将模型代入原数据进行预测
#因为上面的模型的拟合值是对原数据进行稳定化之后的输入数据的拟合，所以需要对拟合值进行相应处理的逆操作，使得它回到与原数据一致的尺度。
#ARIMA拟合的其实是一阶差分ts_log_diff，predictions_ARIMA_diff[i]是第i个月与i-1个月的ts_log的差值。
#由于差分化有一阶滞后，所以第一个月的数据是空的，
predictions_ARIMA_diff = pd.Series(results_AR_values, copy=True)
print('predictions_ARIMA_diff:',predictions_ARIMA_diff.head())
#累加现有的diff，得到每个值与第一个月的差分（同log底的情况下）。
#即predictions_ARIMA_diff_cumsum[i] 是第i个月与第1个月的ts_log的差值。
predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()
#先ts_log_diff => ts_log=>ts_log => ts
#先以ts_log的第一个值作为基数，复制给所有值，然后每个时刻的值累加与第一个月对应的差值(这样就解决了，第一个月diff数据为空的问题了)
#然后得到了predictions_ARIMA_log => predictions_ARIMA
predictions_ARIMA_log = pd.Series(data_label_log.ix[0], index=data_label_log.index)
predictions_ARIMA_log = predictions_ARIMA_log.add(predictions_ARIMA_diff_cumsum,fill_value=0)
predictions_ARIMA = np.exp(predictions_ARIMA_log)
print('predictions_ARIMA',predictions_ARIMA)
plt.figure()
plt.plot(data_label[:300])
plt.plot(predictions_ARIMA[:300])
plt.title('RMSE: %.4f'% np.sqrt(sum((predictions_ARIMA-data_label)**2)/len(data_label)))
print('RMSE: %.4f'% np.sqrt(sum((predictions_ARIMA-data_label)**2)/len(data_label)))
plt.show()
