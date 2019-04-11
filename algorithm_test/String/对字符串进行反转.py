'''实现字符串的反转
'''
def reverseStr(str):
    ch = list(str)
    lens = len(ch)
    i = 0
    j = lens-1
    while i<j:
        tmp=ch[i]
        ch[i]=ch[j]
        ch[j]=tmp
        i+=1
        j-=1
    return ''.join(ch)

str='abcdefg'
print(reverseStr(str))







