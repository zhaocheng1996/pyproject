'''
硬币最小数量
Description
Given the list of coins of distinct denominations and total amount of money. Output the minimum number of coins required to make up that amount. Output -1 if that money cannot be made up using given coins. You may assume that there are infinite numbers of coins of each type.
给出不同面额和总金额的硬币列表。输出构成该金额所需的最少硬币数量。如果使用给定的硬币无法弥补这笔钱，则输出-1。您可以假设每种类型的硬币数量无限。
Input
The first line contains 'T' denoting the number of test cases. Then follows description of test cases. Each cases begins with the two space separated integers 'n' and 'amount' denoting the total number of distinct coins and total amount of money respectively. The second line contains N space-separated integers A1, A2, ..., AN denoting the values of coins.
Constraints:1<=T<=30，1<=n<=100，1<=Ai<=1000，1<=amount<=100000
第一行包含表示测试用例数的“T”。然后是对测试用例的描述。每个案例都以两个空格分隔的整数'n'和'金额'开头，分别表示不同硬币的总数和总金额。
第二行包含N个空格分隔的整数A1，A2，...，AN，表示硬币的值。
约束：1 <= T <= 30,1 <= N <= 100,1 <=艾<= 1000,1 <=量<= 100000
Output
Print the minimum number of coins required to make up that amount or return -1 if it is impossible to make that amount using given coins.
打印弥补该金额所需的最小硬币数量，如果使用给定的硬币无法赚取金额，则返回-1。
Sample Input 1 
2
3 11
1 2 5
2 7
2 6
Sample Output 1
 3
-1

比如例一中dp[0] = 0
dp[1] = 1
dp[2] = min{dp[2-1]}+1
dp[3] = min{dp[3-1],dp[3-2]}+1
dp[4] = min{dp[4-1],dp[4-2]}+1
...
dp[11] = min{11-1},dp[11-2],dp[11-5]}+1
'''


def coinChange(coins, amount):
        n = len(coins)
        # dp[i]表示amount=i需要的最少coin数
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for j in range(n):
                # 只有当硬币面额不大于要求面额数时，才能取该硬币
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)
        # 硬币数不会超过要求总面额数，如果超过，说明没有方案可凑到目标值
        return dp[amount] if dp[amount] <= amount else -1

# T = int(input())
# while(T>0):
#     T -= 1
#     amount = [int(x) for x in input().split()]
#     coin = [int(x) for x in input().split()]
amount = [2,7]
coin = [2,6]
acount = []
for item in amount:
    result = coinChange(coin,item)
    acount.append(result)
    if result == -1:
       print(-1)
    else:
       print(max(acount))
