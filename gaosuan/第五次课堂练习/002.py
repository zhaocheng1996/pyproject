'''
时间分隔
Description
Given arrival and departure times of all trains that reach a railway station. Your task is to find the minimum number of platforms required for the railway station so that no train waits.
Note: Consider that all the trains arrive on the same day and leave on the same day. Also, arrival and departure times must not be same for a train.
考虑到达火车站的所有列车的到达和离开时间。您的任务是找到火车站所需的最少平台数，以便没有火车等待。
注意：考虑所有列车在同一天到达并在同一天离开。此外，火车的到达和离开时间也不一样。
Input
The first line of input contains T, the number of test cases. For each test case, first line will contain an integer N, the number of trains. Next two lines will consist of N space separated time intervals denoting arrival and departure times respectively.
Note: Time intervals are in the 24-hourformat(hhmm), preceding zeros are insignificant. 200 means 2:00.
Consider the example for better understanding of input.
Constraints:1 <= T <= 100，1 <= N <= 1000，1 <= A[i] < D[i] <= 2359
第一行输入包含T，即测试用例的数量。对于每个测试用例，第一行将包含整数N，即列车的数量。接下来的两行将由N个空格分隔的时间间隔组成，分别表示到达和离开时间。
注意：时间间隔为24小时格式（hhmm），前面的零值无关紧要。 200表示2点。
考虑更好地理解输入的示例。
约束：1 <= T <= 100,1 <= N <= 1000,1 <= A [i] <D [i] <= 2359
Output
For each test case, print the minimum number of platforms required for the trains to arrive and depart safely.
对于每个测试用例，打印列车安全到达和离开所需的最少平台数。
Sample Input 1 
 1
6
900  940 950  1100 1500 1800
910 1200 1120 1130 1900 2000
Sample Output 1
 3
'''


def findPlatform(arr, dep, n):
    # Sort arrival and
    # departure arrays
    arr.sort()
    dep.sort()

    # plat_needed indicates
    # number of platforms
    # needed at a time
    plat_needed = 1
    result = 1
    i = 1
    j = 0

    # Similar to merge in
    # merge sort to process
    # all events in sorted order
    while (i < n and j < n):
        # If next event in sorted
        # order is arrival,
        # increment count of
        # platforms needed
        if (arr[i] < dep[j]):
            plat_needed += 1
            i += 1
            # Update result if needed
            if (plat_needed > result):
                result = plat_needed
                # Else decrement count
        # of platforms needed
        else:
            plat_needed -= 1
            j += 1

    return result


# arr = [900, 940, 950, 1100, 1500, 1800]
# dep = [910, 1200, 1120, 1130, 1900, 2000]
# n = len(arr)
#
# print("Minimum Number of Platforms Required = ",
#       findPlatform(arr, dep, n))

tc = int(input())
while (tc > 0):
    tc -= 1
    n = int(input())
    arr = [int(x) for x in input().split()]
    dep = [int(x) for x in input().split()]
    print(findPlatform(arr, dep, n))