'''
按照要求保留数组元素使得和最大
Description
Given an array of N numbers, we need to maximize the sum of selected numbers. At each step, you need to select a number Ai, delete one occurrence of Ai-1 (if exists) and Ai each from the array. Repeat these steps until the array gets empty. The problem is to maximize the sum of selected numbers. 必须从大到小选择元素。
Input
The first line of the input contains T denoting the number of the test cases. For each test case, the first line contains an integer n denoting the size of the array. Next line contains n space separated integers denoting the elements of the array. 数组元素已经按照从小到大顺序排列。
Output
For each test case, the output is an integer displaying the maximum sum of selected numbers.

给定N个数字的数组，我们需要最大化所选数字的总和。 在每一步，您需要选择一个数字Ai，从阵列中删除一次出现的Ai-1（如果存在）和Ai。 重复这些步骤，直到数组变空。 问题是最大化所选数字的总和。必须从大到小选择元素。
输入
输入的第一行包含T，表示测试用例的数量。 对于每个测试用例，第一行包含表示数组大小的整数n。 下一行包含n个空格分隔的整数，表示数组的元素。数组元素已经按照从小到大顺序排列。
产量
对于每个测试用例，输出是一个整数，显示所选数字的最大总和。
Sample Input 1
 1
3
1 2 3 说明先选择3然后删除3和2，最后选择1，结果是1+3=4
Sample Output 1
 4
'''


# Python3 program to Maximize the sum of selected
# numbers by deleting three consecutive numbers.

# function to maximize the sum of
# selected numbers
def maximizeSum(a, n):
    # stores the occurrences of the numbers
    ans = dict.fromkeys(range(0, n + 1), 0)

    # marks the occurrence of every
    # number in the sequence
    for i in range(n):
        ans[a[i]] += 1

    # maximum in the sequence
    maximum = max(a)

    # traverse till maximum and apply
    # the recurrence relation
    for i in range(2, maximum + 1):
        ans[i] = max(ans[i - 1],
                     ans[i - 2] + ans[i] * i)

        # return the ans stored in the
    # index of maximum
    return ans[maximum]


# Driver code
# if __name__ == "__main__":
#     a = [1, 2, 3]
#     n = len(a)
#     print(maximizeSum(a, n))

T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    nums = [int(x) for x in input().split(' ')]
    print(maximizeSum(nums,n))
