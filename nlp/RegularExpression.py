import re

#将正则表达式编译成pattern对象
pattern = re.compile(r'hello.*\!')#hello到后面若干个单词，直到见到了！
#使用pattern匹配文本，获取匹配结果，无法匹配时将返回None
match = pattern.match('hello,hanxiaoyang! How are you?')

if match:
    #使用match获得分组信息
    print(match.group())
