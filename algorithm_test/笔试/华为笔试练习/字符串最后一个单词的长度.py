'''
计算字符串最后一个单词的长度，单词以空格隔开。
输入描述:
一行字符串，非空，长度小于5000。
输出描述:
整数N，最后一个单词的长度。
示例1
输入
hello world
输出
5
'''

import sys
string = sys.stdin.readline().split()
print(len(string[-1]))



