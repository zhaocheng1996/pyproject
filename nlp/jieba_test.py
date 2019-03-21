import jieba
import jieba.posseg as pseg

seq_list = jieba.cut("我在学习自然语言处理",cut_all=True)
print(seq_list)
print("Full Mode:"+"/".join(seq_list))#全模式True

seg_list = jieba.cut("我在学习自然语言处理", cut_all=False)#默认
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式,找最合适的模式

seg_list = jieba.cut("他毕业于上海交通大学，在百度深度学习研究院进行研究")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在哈佛大学深造")  # 搜索引擎模式
print(",".join(seg_list))

#很多时候我们需要针对自己的场景进行分词，会有一些领域内的专有词汇。
#•1.可以用jieba.load_userdict(file_name)加载用户字典
#•2.少量的词汇可以自己用下面方法手动添加：
# ◾用 add_word(word, freq=None, tag=None) 和 del_word(word) 在程序中动态修改词典
#◾用 suggest_freq(segment, tune=True) 可调节单个词语的词频，使其能（或不能）被分出来。
print('/'.join(jieba.cut('如果放到旧字典中将出错。',HMM=False)))
#如果/放到/旧/字典/中将/出错/。
jieba.suggest_freq(('中','将'),True)#少量的可以手调整

print('/'.join(jieba.cut('如果放到旧字典中将出错。',HMM=False)))
#如果/放到/旧/字典/中/将/出错/。




#关键词提取
#基于 TF-IDF 算法的关键词抽取
#import jieba.analyse
#•jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())◾sentence 为待提取的文本
#◾topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20,20个关键词
#◾withWeight 为是否一并返回关键词权重值，默认值为 False
#◾allowPOS 仅包括指定词性的词，默认值为空，即不筛选，形容词，动词等

import jieba.analyse as analyse
lines = open('NBA.txt',encoding='UTF-8').read()
print(' '.join(analyse.extract_tags(lines,topK=20,withWeight=False,allowPOS=())))

lines = open(u'西游记.txt',encoding='gb18030').read()
print(' '.join(analyse.extract_tags(lines)))

import jieba.analyse as analyse
lines = open('NBA.txt',encoding='UTF-8').read()
print("  ".join(analyse.textrank(lines, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))))#动名都要
print("---------------------我是分割线----------------")
print("  ".join(analyse.textrank(lines, topK=20, withWeight=False, allowPOS=('ns', 'n'))))#只要名词


#词性标注
# •jieba.posseg.POSTokenizer(tokenizer=None) 新建自定义分词器，tokenizer 参数可指定内部使用的 jieba.Tokenizer 分词器。jieba.posseg.dt 为默认词性标注分词器。
# •标注句子分词后每个词的词性，采用和 ictclas 兼容的标记法。
# •具体的词性对照表参见计算所汉语词性标记集

words = pseg.cut("我爱自然语言处理")
#print(words)#<generator object cut at 0x000001B47D062D58>
for word,flag in words:
    print('%s %s' % (word,flag))


# 并行分词¶
# 原理：将目标文本按行分隔后，把各行文本分配到多个 Python 进程并行分词，然后归并结果，从而获得分词速度的可观提升 基于 python 自带的 multiprocessing 模块，
# 目前暂不支持 Windows
# 用法：
# jieba.enable_parallel(4) # 开启并行分词模式，参数为并行进程数
# jieba.disable_parallel() # 关闭并行分词模式
# 实验结果：在 4 核 3.4GHz Linux 机器上，对金庸全集进行精确分词，获得了 1MB/s 的速度，是单进程版的 3.3 倍。
# 注意：并行分词仅支持默认分词器 jieba.dt 和 jieba.posseg.dt。






