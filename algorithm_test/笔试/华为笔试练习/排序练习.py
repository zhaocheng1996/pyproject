# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         print(values)
#         for v in values:
#             ans += v
#         print(ans)
#     print(ans)

# import sys
# n = int(sys.stdin.readline())
# value = 0
# while n>0:
#     n-=1
#     x = [int(i) for i in sys.stdin.readline().split()]
#     value += sum(x)
# print(value)

'''
长度为n的数组乱序存放着0至n-1. 现在只能进行0与其他数的交换，
'''

