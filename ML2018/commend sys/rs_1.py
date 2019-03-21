"""
基于协同算法的电影推荐系统
"""
#此网址详细的描述了这篇test的细节
# https://blog.csdn.net/qq_20412595/article/details/82558978
# from surprise import KNNBasic,SVD
# from surprise import Dataset
# from surprise import evaluate, print_perf
# # http://surprise.readthedocs.io/en/stable/index.html
# # http://files.grouplens.org/datasets/movielens/ml-100k-README.txt
#
# # Load the movielens-100k dataset (download it if needed),
# # and split it into 3 folds for cross-validation.
# data = Dataset.load_builtin('ml-100k')
# # k折交叉验证(k=3)
# data.split(n_folds=3)
#
# # We'll use the famous KNNBasic algorithm.
# algo = KNNBasic()#基本的协同过滤算法
#
# # Evaluate performances of our algorithm on the dataset.
# perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
#
# print_perf(perf)

#算法调参
# from surprise import GridSearch
# # 定义好需要优选的参数网格
# param_grid = {'n_epochs': [5, 10], 'lr_all': [0.002, 0.005],
#               'reg_all': [0.4, 0.6]}
# #n_epochs训练批次的大小，lr_all全局学习率，
# # 使用网格搜索交叉验证
# grid_search = GridSearch(SVD, param_grid, measures=['RMSE', 'FCP'])
# # 在数据集上找到最好的参数
# data = Dataset.load_builtin('ml-100k')
# data.split(n_folds=3)
# grid_search.evaluate(data)

# 输出调优的参数组
# 输出最好的RMSE结果
#print(grid_search.best_score['RMSE'])
# >>> 0.96117566386

# 输出对应最好的RMSE结果的参数
#print(grid_search.best_params['RMSE'])
# >>> {'reg_all': 0.4, 'lr_all': 0.005, 'n_epochs': 10}

# 最好的FCP得分,FCP一致对的概率
#print(grid_search.best_score['FCP'])
# >>> 0.702279736531

# 对应最高FCP得分的参数
#print(grid_search.best_params['FCP'])
# >>> {'reg_all': 0.6, 'lr_all': 0.005, 'n_epochs': 10}

# import pandas as pd
#
# results_df = pd.DataFrame.from_dict(grid_search.cv_results)
# print(results_df)



# 可以使用上面提到的各种推荐系统算法
from surprise import SVD
from surprise import Dataset
from surprise import evaluate, print_perf

# 默认载入movielens数据集
data = Dataset.load_builtin('ml-100k')
# k折交叉验证(k=3)
data.split(n_folds=3)
# 试一把SVD矩阵分解
algo = SVD()
# 在数据集上测试一下效果
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
# 输出结果
print_perf(perf)

"""
以下的程序段告诉大家如何在协同过滤算法建模以后，根据一个item取回相似度最高的item，主要是用到algo.get_neighbors()这个函数
"""

#from __future__ import (absolute_import, division, print_function,
#                        unicode_literals)
import os
import io

from surprise import KNNBaseline
from surprise import Dataset
def read_item_names():
    """
    获取电影名到电影id 和 电影id到电影名的映射
    """

    file_name = (os.path.expanduser('~') +
                 '/.surprise_data/ml-100k/ml-100k/u.item')
    rid_to_name = {}
    name_to_rid = {}
    with io.open(file_name, 'r', encoding='ISO-8859-1') as f:
        for line in f:
            line = line.split('|')
            rid_to_name[line[0]] = line[1]
            name_to_rid[line[1]] = line[0]

    return rid_to_name, name_to_rid


# 首先，用算法计算相互间的相似度
data = Dataset.load_builtin('ml-100k')
trainset = data.build_full_trainset()
sim_options = {'name': 'pearson_baseline', 'user_based': False}
algo = KNNBaseline(sim_options=sim_options)#考虑了基础评分的协同过滤算法
algo.train(trainset)

# 获取电影名到电影id 和 电影id到电影名的映射
rid_to_name, name_to_rid = read_item_names()

# Retieve inner id of the movie Toy Story
toy_story_raw_id = name_to_rid['Toy Story (1995)']
toy_story_inner_id = algo.trainset.to_inner_iid(toy_story_raw_id)

# Retrieve inner ids of the nearest neighbors of Toy Story.
toy_story_neighbors = algo.get_neighbors(toy_story_inner_id, k=10)

# Convert inner ids of the neighbors into names.
toy_story_neighbors = (algo.trainset.to_raw_iid(inner_id)
                       for inner_id in toy_story_neighbors)
toy_story_neighbors = (rid_to_name[rid]
                       for rid in toy_story_neighbors)

print()
print('The 10 nearest neighbors of Toy Story are:')
for movie in toy_story_neighbors:
    print(movie)





