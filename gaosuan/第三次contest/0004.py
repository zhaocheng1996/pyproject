'''
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.
给定文本txt [0..n-1]和模式pat [0..m-1]，编写一个函数搜索（char pat []，char txt []），在txt中打印所有出现的pat [][]。 你可以假设n> m。
Input
输入第一行是用例个数，后面一行表示一个用例；用例包括两部分，第一部分为给定文本，第二部分为搜索串，两部分使用","隔开。
Output
每一个用例输出一行，每行按照找到的位置先后顺序排列，使用空格隔开。
Sample Input 1 
 2
THIS IS A TEST TEXT,TEST
AABAACAADAABAABA,AABA
Sample Output 1
 10
0 9 12
'''


def search(pat, txt):
    M = len(pat)
    N = len(txt)

    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0

        # For current index i, check
        # for pattern match */
        for j in range(0, M):
            if (txt[i + j] != pat[j]):
                break

        if (j == M - 1):
            return " ".join(i)


        # txt = "ABABDABACDABABCABAB"
# pat = "ABABCABAB"
# KMPSearch(pat, txt)

n = int(input())
for i in range(0,n):
    result = []
    arr = input()
    txt,pat = arr.split(",")
    #print(txt,pat)
    result1 = search(pat,txt)
    result.append(result1)
    print(result)
