import re
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
#print(result)#<_sre.SRE_Match object; span=(0, 41), match='Hello 123 4567 World_This is a Regex Demo'>
#print(result.group())#返回匹配结果
#print(result.span())#(0, 41)结果范围

#泛匹配
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$',content)#.*可以匹配到所有的字符
#print(result)

#匹配目标
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s\d+\sWorld.*Demo$',content)
print(result)
#print(result.group())

content = ' 12345 '
result = re.match('^\s\d+\s',content)
print(result)

#贪婪匹配
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$',content)
print(result)
print(result.group(1))#输出为7，由于d+是至少匹配一个数字，这里.*就匹配了所有的7前面的数字

#非贪婪模式
result = re.match('^He.*?(\d+).*Demo$',content)#.*?
print(result)
print(result.group(1))#输出为：1234567

content =  'Hello 1234567 World_This ' \
           'is a Regex Demo'


#转义
content = 'price is $5.00'
result = re.match('price is \$5\.00',content)
print(result)

#re.sub 替换字符串中每一个匹配的子串后返回替换的字符串
content = 'Extro stings Hello 1234567 World_This is a Regex Demo Extra stings'
content = re.sub('\d+','',content)
print(content)#Extro stings Hello  World_This is a Regex Demo Extra stings

#re.compile 将一个正则表达式串编译成正则对象，以便于复用该匹配模式
content = 'Hello 1234567 World_This ' \
'is a Regex Demo'

patten = re.compile("Hello.*Demo",re.S)
result = re.match(patten,content)
print(result)#<_sre.SRE_Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>








