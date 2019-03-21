'''
Given an array of positive integers and many queries for divisibility. In every query Q[i], we are given an integer K , we need to count all elements in the array which are perfectly divisible by K.
Constraints:1<=T<=1001<=N,M<=1051<=A[i],Q[i]<=105
给出一组正整数和许多可分解的查询。 在每个查询Q [i]中，我们给出一个整数K，我们需要计算数组中所有可被K完全整除的元素。
Input
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of three lines. First line of each test case contains two integers N & M, second line contains N space separated array elements and third line contains M space separated queries.
第一行输入包含一个整数T，表示测试用例的数量。 然后是T测试案例。 每个测试用例由三行组成。 每个测试用例的第一行包含两个整数N和M，第二行包含N个空格分隔的数组元素，第三行包含M个空格分隔的查询。
Output
For each test case,In new line print the required count for each query Q[i].
Sample Input 1
 2
6 3
2 4 9 15 21 20
2 3 5
3 2
3 4 6
2 3
Sample Output 1
 3 3 2
2 2
'''

# Python3 program to calculate all multiples
# of integer 'k' in array[]

# ans is global array so that both countSieve()
# and countMultiples() can access it.
ans = []


# Function to pre-calculate all multiples
# of array elements
# Here, the arguments are as follows
# a: given array
# n: length of given array
def countSieve(arr, n):
    MAX = max(arr)

    # Accessing the global array in the function
    global ans

    # Initializing "ans" array with zeros
    ans = [0] * (MAX + 1)

    # Initializing "cnt" array with zeros
    cnt = [0] * (MAX + 1)

    # Store the arr[] elements as index in cnt[] array
    for i in range(n):
        cnt[arr[i]] += 1

    # Iterate over all multiples as 'i'
    # and keep the count of array[] ( In
    # cnt[] array) elements in ans[] array
    for i in range(1, MAX + 1):
        for j in range(i, MAX + 1, i):
            ans[i] += cnt[j]


def countMultiples(k):
    # Return pre-calculated result
    return (ans[k])


# Driver code
# if __name__ == "__main__":
#     arr = [2, 4, 9, 15, 21, 20]
#     n = len(arr)
#     # Pre-calculate all multiples
#     countSieve(arr, n)
#     k = 2
#     print(countMultiples(2))
#     k = 3
#     print(countMultiples(3))
#     k = 5
#     print(countMultiples(5))

n=int(input())
for i in range(0,n):
    number = input()
    #print(number)
    number_split = number.split()
    number_int = list(map(int,number_split))
    arr1 = input()
    arr1_split = arr1.split()
    arr1_int = list(map(int,arr1_split))
    n1 = len(arr1_int)
    countSieve(arr1_int,n1)
    #print(arr1)
    arr2 = input()
    arr2_split = arr2.split()
    arr2_int = list(map(int,arr2_split))
    result = []
    for item in arr2_int:
        result1=countMultiples(item)
        result.append(result1)
    #print(result)

    #print(arr2)
