'''
实现一个求字符串中连续出现相同字符的最大值，例如字符串“aaabbcc”
 中连续出现字符＇a’的最大值为 3，字符串“abbc”中连续出现字符＇b＇的最大值为 2
'''

def getMaxDupChars(s):
    curMaxlen=1
    maxLen=-1
    i=0
    while i<len(s)-1:
       if s[i]==s[i+1]:
           curMaxlen+=1
           maxLen=max(curMaxlen,maxLen)
       else:
           curMaxlen=0
       i+=1
    return maxLen
print(getMaxDupChars('aaabbccc'))




