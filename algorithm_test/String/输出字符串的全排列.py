'''
输入一个字符串时，输出这个字符串的所有排列。例如输入字符串abc,要求
输出由字符串a，b,c所能排出来的所有字符串：abc，acb，bac，bca，cba，acb
：递归法 下面以字符串 abc 为例介绍对字符串进行全排列的方法。 具体步骤如下：
第一步是确定第一个位置的字符，就是第一个位置与后边的所有字符进行交换。
第二步，就是对除了第一个位置的后边所有位置的字符进行相同处理；直至剩下一个字符
递归的出口，就是只剩一个字符的时候，递归的循环过程，就是从每个子串的第二个字符开始依次与第一个字符交换，
然后继续处理子串，如果有重复的，然后对结果使用set去重就可以了
'''

def perm(s=''):
    if len(s)<=1:
        return [s]
    sl = []
    for i in range(len(s)):
        for j in perm(s[0:i]+s[i+1:]):
            sl.append(s[i] + j)
    return sl

#可能包含重复的串
perm_nums = perm('abc')
np_reapt_nums = list(set(perm_nums))
print('per_nums',len(perm_nums),perm_nums)
print('no_repeat_nums',len(np_reapt_nums),np_reapt_nums)

















