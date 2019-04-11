'''
判断包含两个字符串的包含关系
'''

#直接法
def isContain(str1,str2):
    len1 = len(str1)
    len2 = len(str2)
    i=0
    while i < len2:
       j=0
       while j< len1:
           if str1[j]==str2[i]:
               break
           else:
               j+=1
           if j>=len1:
               return False
       i+=1
       if i==len2:
            return True
str1 = 'abcdef'
str2 = 'acfx'
isContain = isContain(str1,str2)
if isContain:
    print('有包含关系')
else:
    print('没包含关系')









