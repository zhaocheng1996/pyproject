'''
最长公共子序列
Description
给定两个字符串，返回两个字符串的最长公共子序列（不是最长公共子字符串），可能是多个。
Input
输入为两行，一行一个字符串
Output
输出如果有多个则分为多行，先后顺序不影响判断。
Sample Input 1 
1A2BD3G4H56JK
23EFG4I5J6K7
Sample Output 1
23G456K
23G45JK
'''

# import numpy
# def find_lcseque(s1, s2):
#     # 生成字符串长度加1的0矩阵，m用来保存对应位置匹配的结果
#     m = [[0 for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]
#     # d用来记录转移方向
#     d = [[None for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]
#
#     for p1 in range(len(s1)):
#         for p2 in range(len(s2)):
#             if s1[p1] == s2[p2]:  # 字符匹配成功，则该位置的值为左上方的值加1
#                 m[p1 + 1][p2 + 1] = m[p1][p2] + 1
#                 d[p1 + 1][p2 + 1] = 'ok'
#             elif m[p1 + 1][p2] > m[p1][p2 + 1]:  # 左值大于上值，则该位置的值为左值，并标记回溯时的方向
#                 m[p1 + 1][p2 + 1] = m[p1 + 1][p2]
#                 d[p1 + 1][p2 + 1] = 'left'
#             else:  # 上值大于左值，则该位置的值为上值，并标记方向up
#                 m[p1 + 1][p2 + 1] = m[p1][p2 + 1]
#                 d[p1 + 1][p2 + 1] = 'up'
#     (p1, p2) = (len(s1), len(s2))
#     print
#     numpy.array(d)
#     s = []
#     while m[p1][p2]:  # 不为None时
#         c = d[p1][p2]
#         if c == 'ok':  # 匹配成功，插入该字符，并向左上角找下一个
#             s.append(s1[p1 - 1])
#             p1 -= 1
#             p2 -= 1
#         if c == 'left':  # 根据标记，向左找下一个
#             p2 -= 1
#         if c == 'up':  # 根据标记，向上找下一个
#             p1 -= 1
#     s.reverse()
#     return ''.join(s)
#
#
# print(find_lcseque('1A2BD3G4H56JK', '23EFG4I5J6K7'))
#
#
# def LCS(x,y):
#     import numpy as np
#     c=np.zeros((len(x)+1,len(y)+1))
#     b=np.zeros((len(x)+1,len(y)+1))
#     for i in range(1,len(x)+1):
#         for j in range(1,len(y)+1):
#             if x[i-1]==y[j-1]:
#                 c[i,j]=c[i-1,j-1]+1
#                 b[i,j]=2
#             else:
#                 if c[i-1,j]>=c[i,j-1]:
#                     c[i,j]=c[i-1,j]
#                     b[i,j]=1
#                 else:
#                     c[i,j]=c[i,j-1]
#                     b[i,j]=3
#     return c,b
#
# def getLCS(x,y):
#     c,b=LCS(x,y)
#     i=len(x)
#     j=len(y)
#     lcs=''
#     while i>0 and j>0:
#         if b[i][j]==2:
#             lcs=x[i-1]+lcs
#             i-=1
#             j-=1
#         if b[i][j]==1:
#             i-=1
#         if b[i][j]==3:
#             j-=1
#         if b[i][j]==0:
#             break
#     return lcs
#
# print(getLCS("1A2BD3G4H56JK","23EFG4I5J6K7"))
#
#
# def LCS(x, y):
#     d = [[None for i in x] for j in y]
#     m = [[0 for k in x] for v in y]
#     for p1 in range(len(y)):
#         for p2 in range(len(x)):
#             if y[p1] == x[p2]:
#                 if p1 == 0 or p2 == 0:
#                     m[p1][p2] = 1
#                 else:
#                     m[p1][p2] = m[p1 - 1][p2 - 1] + 1
#                 d[p1][p2] = 1
#             elif m[p1 - 1][p2] < m[p1][p2 - 1]:
#                 m[p1][p2] = m[p1][p2 - 1]
#                 d[p1][p2] = 2
#             else:  # m[p1][p2-1] < m[p1-1][p2]
#                 m[p1][p2] = m[p1 - 1][p2]
#                 d[p1][p2] = 3
#
#     s = []
#     (p1, p2) = (len(y) - 1, len(x) - 1)
#     while p1 >= 0 and p2 >= 0 and m[p1][p2] > 0:
#         print(p1, p2)
#         c = d[p1][p2]
#         if c == 1:
#             s.append(y[p1])
#             p1 -= 1
#             p2 -= 1
#         if c == 2: p2 -= 1
#         if c == 3: p1 -= 1
#     s.reverse()
#     return s
#
#
#
# x = "1A2BD3G4H56JK"
# y = "23EFG4I5J6K7"
# LCS = LCS(x, y)
# for item in LCS:
#     print(" ".join(item))

li = []
class LCS():
    global li
    def input(self, x, y):
    #读入待匹配的两个字符串
        if type(x) != str or type(y) != str:
            print('input error')
            return None
        self.x = x
        self.y = y

    def Compute_LCS(self):
        xlength = len(self.x)
        ylength = len(self.y)
        self.direction_list = [None] * xlength #这个二维列表存着回溯方向
        for i in range(xlength):
            self.direction_list[i] = [None] * ylength
        self.lcslength_list = [None] * (xlength + 1)
        #这个二维列表存着当前最长公共子序列长度
        for j in range(xlength + 1):
            self.lcslength_list[j] = [None] * (ylength + 1)

        for i in range(0, xlength + 1):
            self.lcslength_list[i][0] = 0
        for j in range(0, ylength + 1):
            self.lcslength_list[0][j] = 0
        #下面是进行回溯方向和长度表的赋值
        for i in range(1, xlength + 1):
            for j in range(1, ylength + 1):
                if self.x[i - 1] == self.y[j - 1]:
                    self.lcslength_list[i][j] = self.lcslength_list[i - 1][j - 1] + 1
                    self.direction_list[i - 1][j - 1] = 0  # 左上
                elif self.lcslength_list[i - 1][j] > self.lcslength_list[i][j - 1]:
                    self.lcslength_list[i][j] = self.lcslength_list[i - 1][j]
                    self.direction_list[i - 1][j - 1] = 1  # 上
                elif self.lcslength_list[i - 1][j] < self.lcslength_list[i][j - 1]:
                    self.lcslength_list[i][j] = self.lcslength_list[i][j - 1]
                    self.direction_list[i - 1][j - 1] = -1  # 左
                else:
                    self.lcslength_list[i][j] = self.lcslength_list[i - 1][j]
                    self.direction_list[i - 1][j - 1] = 2  # 左或上
        self.lcslength = self.lcslength_list[-1][-1]
        return self.direction_list, self.lcslength_list


    def printLCS(self, curlen, i, j, s):
        if i == 0 or j == 0:
            return None

        if self.direction_list[i - 1][j - 1] == 0:
            if curlen == self.lcslength:
                s += self.x[i - 1]
                # print(s[::-1])
                li.append(s[::-1])
                # print(set(li))
                # for i in range(len(s)-1,-1,-1):
                #     print(s[i])

            elif curlen < self.lcslength:
                s += self.x[i-1]
                self.printLCS(curlen + 1, i - 1, j - 1, s)
        elif self.direction_list[i - 1][j - 1] == 1:
            self.printLCS(curlen,i - 1, j,s)
        elif self.direction_list[i - 1][j - 1] == -1:
            self.printLCS(curlen,i, j - 1,s)
        else:
            self.printLCS(curlen,i - 1, j,s)
            self.printLCS(curlen,i, j - 1,s)


    def returnLCS(self):
        #回溯的入口
        self.printLCS(1,len(self.x), len(self.y),'')
        # return li

if __name__ == '__main__':
    str1 = input()
    str2 = input()
    p = LCS()
    p.input(str1, str2)
    p.Compute_LCS()
    p.returnLCS()
    for i in set(li):
        print(i)