#新闻分类
import os
import time
import random
import jieba
import nltk
import sklearn
from sklearn.naive_bayes import MultinomialNB #多项式朴素贝叶斯
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

#词去重
def make_word_set(words_file):
    words_set = set()
    with open(words_file,'r',encoding='gb18030',errors='ignore') as fp:
        for line in fp.readlines():
            word = line.strip().encode("utf-8")#每行移除首尾空格【
            if len(word)>0 and word not in words_set:
                words_set.add(word)
    return  words_set

#文本处理，也就是样本生成过程
def text_processing(folder_path,test_size=0.2):
    folder_list = os.listdir(folder_path)
    data_list = []
    class_list = []

    # 遍历文件夹
    for folder in folder_list:
        new_folder_path = os.path.join(folder_path,folder)#路径拼接，从后往前看，会从第一个以“/”开头的参数开始拼接，他之前的参数全部丢弃。
        files = os.listdir(new_folder_path)#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
        #读取文件
        j = 1
        for file in files:
            if j>100: #只取100个样本文件
                break
            with open(os.path.join(new_folder_path,file),'r',encoding='gb18030',errors='ignore') as fp:
                raw = fp.read()
            #jieba.enble_parallel(4)#开启并行分词模式，参数为并行进程数
            word_cut = jieba.cut(raw,cut_all=False)#精确模式，返回结构是一个可迭代的genertor
            word_list = list(word_cut)#转化为list，每个词unicode格式
            data_list.append(word_list)#训练集
            class_list.append(folder.encode('utf-8'))#用tuf—8来解码

    #划分测试集和训练集
    data_class_list = list(zip(data_list, class_list))
    random.shuffle(data_class_list)#将类别标签随机排序
    index = int(len(data_class_list) * test_size) + 1
    train_list = data_class_list[index:]
    test_list = data_class_list[:index]
    train_data_list, train_class_list = list(zip(*train_list))
    test_data_list, test_class_list = list(zip(*test_list))

    #统计词频放入all_words_dict
    all_word_dict = {}
    for word_list in train_data_list:
        for word in word_list:
            if all_word_dict.__contains__(word):
                all_word_dict[word] += 1
            else:
                all_word_dict[word] = 1

    # Key函数利用词频进行降序排序
    all_words_tuple_list = sorted(all_word_dict.items(), key=lambda f: f[1], reverse=True)  # 内建函数sorted参数需为list
    all_words_list = list(zip(*all_words_tuple_list))[0]

    return all_words_list, train_data_list, test_data_list, train_class_list, test_class_list

def words_dict(all_words_list, deleteN, stopwords_set=set()):
    # 选取特征词
    feature_words = []
    n = 1
    for t in range(deleteN, len(all_words_list), 1):
        if n > 1000:  # feature_words的维度1000
            break
            #isdigit()如果字符串只包含数字则返回 True 否则返回 False。
        if not all_words_list[t].isdigit() and all_words_list[t] not in stopwords_set and 1 < len(
                all_words_list[t]) < 5:
            feature_words.append(all_words_list[t])
            n += 1
    return feature_words

# 文本特征
def text_features(train_data_list, test_data_list, feature_words, flag='nltk'):
    def text_features(text, feature_words):
        text_words = set(text)
        ## -----------------------------------------------------------------------------------
        if flag == 'nltk':
            ## nltk特征 dict
            features = {word:1 if word in text_words else 0 for word in feature_words}#如果出现了就记1，没出现就记0
        elif flag == 'sklearn':
            ## sklearn特征 list
            features = [1 if word in text_words else 0 for word in feature_words]
        else:
            features = []
        ## -----------------------------------------------------------------------------------
        return features
    train_feature_list = [text_features(text, feature_words) for text in train_data_list]
    test_feature_list = [text_features(text, feature_words) for text in test_data_list]
    return train_feature_list, test_feature_list

# 分类，同时输出准确率等
def text_classifier(train_feature_list, test_feature_list, train_class_list, test_class_list, flag='nltk'):
    ## -----------------------------------------------------------------------------------
    if flag == 'nltk':
        ## 使用nltk分类器
        train_flist = list(zip(train_feature_list, train_class_list))
        test_flist = list(zip(test_feature_list, test_class_list))
        classifier = nltk.classify.NaiveBayesClassifier.train(train_flist)
        test_accuracy = nltk.classify.accuracy(classifier, test_flist)
    elif flag == 'sklearn':
        ## sklearn分类器
        classifier = MultinomialNB().fit(train_feature_list, train_class_list)
        test_accuracy = classifier.score(test_feature_list, test_class_list)
    else:
        test_accuracy = []
    return test_accuracy

print("start")

## 文本预处理
#folder_path = './Database/SogouC/Sample'
folder_path = 'E:/Python学习/0、2017年七月在线：自然语言处理班（从基础算法到实战应用）/2\Lecture_2/Lecture_2/Naive-Bayes-Text-Classifier/Database/SogouC/Sample'
all_words_list, train_data_list, test_data_list, train_class_list, test_class_list = text_processing(folder_path, test_size=0.2)

# 生成stopwords_set
stopwords_file = 'E:/Python学习/0、2017年七月在线：自然语言处理班（从基础算法到实战应用）/2/Lecture_2/Lecture_2/Naive-Bayes-Text-Classifier/stopwords_cn.txt'
stopwords_set = make_word_set(stopwords_file)

## 文本特征提取和分类
# flag = 'nltk'
flag = 'sklearn'
deleteNs = range(0, 1000, 20)
test_accuracy_list = []
for deleteN in deleteNs:
    # feature_words = words_dict(all_words_list, deleteN)
    feature_words = words_dict(all_words_list, deleteN, stopwords_set)
    train_feature_list, test_feature_list = text_features(train_data_list, test_data_list, feature_words, flag)
    test_accuracy = text_classifier(train_feature_list, test_feature_list, train_class_list, test_class_list, flag)
    test_accuracy_list.append(test_accuracy)
print(test_accuracy_list)

# 结果评价
#plt.figure()
plt.plot(deleteNs, test_accuracy_list)
plt.title('Relationship of deleteNs and test_accuracy')
plt.xlabel('deleteNs')
plt.ylabel('test_accuracy')
plt.show()
#plt.savefig('result.png')

print("finished")












