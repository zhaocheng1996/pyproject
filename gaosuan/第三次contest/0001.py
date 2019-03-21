'''
字符串1
Description
Given a string ‘str’ of digits, find length of the longest substring of ‘str’, such that the length of the substring is 2k digits and sum of left k digits is equal to the sum of right k digits.
Input
输入第一行是测试用例的个数，后面每一行表示一个数字组成的字符串，例如："123123"
Output
输出找到的满足要求的最长子串的长度。例如，给定的例子长度应该是 6。每行对应一个用例的结果。
Sample Input 1
 1
1538023
Sample Output 1
 4
'''


def findLength(str):
    n = len(str)
    maxlen = 0  # Initialize result

    # Choose starting point
    # of every substring
    for i in range(0, n):

        # Choose ending point
        # of even length substring
        for j in range(i + 1, n, 2):

            # Find length of current substr
            length = j - i + 1

            # Calculate left & right
            # sums for current substr
            leftsum = 0
            rightsum = 0
            for k in range(0, int(length / 2)):
                leftsum += (int(str[i + k]) - int('0'))
                rightsum += (int(str[i + k + int(length / 2)]) - int('0'))

                # Update result if needed
            if (leftsum == rightsum and maxlen < length):
                maxlen = length

    return maxlen

arr = "1538023"
print(findLength(arr))
# n = int(input())
# for i in range(0,n):
#     arr = input()
# #arr = '1538023'
#     #arr_split = arr.split()
#     arr_split_int = list(map(int, arr))
#     #print(arr_split_int)
#     print(findLength(arr_split_int))
