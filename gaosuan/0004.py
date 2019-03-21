
# 汉诺塔
# Description
# 汉诺塔问题中限制不能将一层塔直接从最左侧移动到最右侧，
# 也不能直接从最右侧移动到最左侧，而是必须经过中间。求当有N层塔的时候移动步数。
# Input输入的第一行为N。
# Output移动步数。
# Sample Input 1 2
# out 8
'''
n-1层只需要移动两次，从左到中，从中到右，最上面一层需要移动三个来回，从左到右，再从右到左，最后再左
'''

num = int(input())

def hannoi(num):
    if num == 1:
        return 2
    return 3*hannoi(num-1)+2

#print(hannoi(3))





