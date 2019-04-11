'''
判断一个字符串是否包含重复字符串

'''

#蛮力

def isDup(s):
    i=0
    while i<len(s):
        j=i+1
        while j < len(s):
            if s[i] == s[j]:
                return True
            else:
                j+=1
        i+=1
    return False

strs = 'GOD'
res = isDup(strs)
print(res)



















