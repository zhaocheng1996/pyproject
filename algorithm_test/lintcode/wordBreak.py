'''
给定字符串s和单词字典dict，确定s是否可以分成一个或多个字典单词的空格分隔序列。
Example 1:
	Input:  "lintcode", ["lint", "code"]
	Output:  true

Example 2:
	Input: "a", ["a"]
	Output:  true
'''
#首先想到的是暴力破解，我们通过索引遍历字符串，测试本次遍历到的s[pre:cur]是不是wordDict中的字符串，
#不是的话cur+1继续判断，否则我们pre=cur，直到cur=len(s)。

def wordBreak(s,dict):
    len_s = len(s)
    cur = 1
    per = 0
    while cur != len_s:
        if s[per:cur] in dict:
            per = cur
        else:
            cur += 1
    if s[per:cur] in dict:
        return True
    else:
        return False

s = 'leetcode'
dict = ["leet", "code"]
print(wordBreak(s,dict))



