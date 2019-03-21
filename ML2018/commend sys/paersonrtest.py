#皮尔逊相关系数计算
import numpy as np
a = np.array([[1, 1, 2, 2, 3],
       [2, 2, 3, 3, 5],
       [1, 4, 2, 2, 3]])
#使用np.corrcoef(a)可计算行与行之间的相关系数
paersoner = np.corrcoef(a)
print(paersoner)
#np.corrcoef(a,rowvar=0)用于计算各列之间的相关系数
p2 = np.corrcoef(a,rowvar=0)
print(p2)
