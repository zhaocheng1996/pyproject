'''
订单问题
Rahul and Ankit are the only two waiters in Royal Restaurant. Today, the restaurant received N orders. The amount of tips may differ when handled by different waiters, if Rahul takes the ith order, he would be tipped Ai rupees and if Ankit takes this order, the tip would be Bi rupees.In order to maximize the total tip value they decided to distribute the order among themselves. One order will be handled by one person only. Also, due to time constraints Rahul cannot take more than X orders and Ankit cannot take more than Y orders. It is guaranteed that X + Y is greater than or equal to N, which means that all the orders can be handled by either Rahul or Ankit. Find out the maximum possible amount of total tip money after processing all the orders.
Input
• The first line contains one integer, number of test cases.
• The second line contains three integers N, X, Y.
• The third line contains N integers. The ith integer represents Ai.
• The fourth line contains N integers. The ith integer represents Bi.
Output
Print a single integer representing the maximum tip money they would receive.
Sample Input 1 
 1
5 3 3
1 2 3 4 5
5 4 3 2 1
Sample Output 1
 21
Rahul和Ankit是皇家餐厅唯一的两位服务员。今天，餐厅收到了N个订单。当由不同的服务员处理时，提示量可能会有所不同，
如果Rahul采用第i个订单，他将被给予Ai rupees，如果Ankit接受此订单，则提示将是Bi rupees。
为了最大化总提示值，他们决定在他们自己之间分配订单。一个订单仅由一个人处理。另外，由于时间限制，Rahul不能超过X订单而且Ankit不能超过Y订单。
保证X + Y大于或等于N，这意味着所有订单都可以由Rahul或Ankit处理。在处理完所有订单后，找出最大可能的总额金额。
输入
•第一行包含一个整数，多个测试用例。
•第二行包含三个整数N，X，Y。
•第三行包含N个整数。第i个整数表示Ai。
•第四行包含N个整数。第i个整数表示Bi。
产量
打印一个整数，表示他们将收到的最大小费。

'''

tc = int(input())
dict = {}
def get_val(i, x, y):
    if (i, x, y) in dict:
        return dict[(i, x, y)]
    if (i == 0):
        if (x == 0):
            dict[(i, x, y)] = b[i]
        elif (y == 0):
            dict[(i, x, y)] = a[i]
        else:
            dict[(i, x, y)] = max(a[i], b[i])
        return dict[(i, x, y)]
    if (x == 0):
        dict[(i, x, y)] = b[i] + get_val(i - 1, x, y - 1)
    elif y == 0:
        dict[(i, x, y)] = a[i] + get_val(i - 1, x - 1, y)
    else:
        dict[(i, x, y)] = max(a[i] + get_val(i - 1, x - 1, y), b[i] + get_val(i - 1, x, y - 1))
    return dict[(i, x, y)]


while (tc > 0):
    tc -= 1
    dict.clear()
    n, x, y = input().split()
    n = int(n)
    x = int(x)
    y = int(y)
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    print(get_val(n - 1, x, y))


