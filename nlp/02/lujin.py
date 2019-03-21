import os
import jieba
import random

def make_word_set(words_file):
    words_set = set()
    with open(words_file,'r',encoding='gb18030',errors='ignore') as fp:
        for line in fp.readlines():
            word = line.strip().encode("utf-8")#每行移除首尾空格【
            if len(word)>0 and word not in words_set:
                words_set.add(word)
    return  words_set

# 生成stopwords_set
stopwords_file = 'E:/Python学习/0、2017年七月在线：自然语言处理班（从基础算法到实战应用）/2/Lecture_2/Lecture_2/Naive-Bayes-Text-Classifier/stopwords_cn.txt'
stopwords_set = make_word_set(stopwords_file)
print(stopwords_set)

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

folder_path = 'E:/Python学习/0、2017年七月在线：自然语言处理班（从基础算法到实战应用）/2\Lecture_2/Lecture_2/Naive-Bayes-Text-Classifier/Database/SogouC/Sample'
all_words_list, train_data_list, test_data_list, train_class_list, test_class_list = text_processing(folder_path, test_size=0.2)
print(all_words_list)
print(train_data_list)