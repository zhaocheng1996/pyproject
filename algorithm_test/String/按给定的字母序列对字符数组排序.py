'''
己知字母序列［d, g, e, c, f, b, o, a］，请实现一个方法，要求对输入的一组字符串
input=［“bed”，“dog“，“dear”，“eye＂］按照字母顺序排序井打印。
本例的输出顺序为： dear, dog,eye, bed
'''

rule = 'dgecfboa'
lens = len(rule)
char_to_int = dict()
#根据给定字符序列构造字典
i=0
while i<lens:
    char_to_int[rule[i]] = i
    i+=1
print(char_to_int)

def compare(str1,str2,char_to_int):
    len1 = len(str1)
    len2 = len(str2)
    i = 0
    j = 0
    while i <len1 and j<len2:
        if str1[i] not in char_to_int.keys():
            char_to_int[str1[i]]=-1
        if str2[j] not in char_to_int.keys():
            char_to_int[str2[j]]=-1
        #比较各个字符的大小
        if char_to_int[str1[i]]<char_to_int[str2[j]]:
            return -1
        elif char_to_int[str1[i]]>char_to_int[str2[j]]:
            return 1
        else:
            i+=1
            j+=1
    if i==len1 and j==len2:
        return 0
    elif i==len1:
        return -1
    else:
        return 1

def insertSort(s,char_to_int):
    lens = len(s)
    i=1
    while i<lens:
       temp = s[i]
       j=i-1
       while j>=0:
           if compare(temp,s[j],char_to_int)==-1:
               s[j+1]=s[j]
           else:
               break
           j-=1
       s[j+1] = temp
       i+=1

s=['bed','dog','dear','eye']
insertSort(s,char_to_int)
i=0
while i<len(s):
    print(s[i],end=' ')
    i+=1












