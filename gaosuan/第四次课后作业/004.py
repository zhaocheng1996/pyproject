'''
生活日常之蔬菜购买
Description
Rahul wanted to purchase vegetables mainly brinjal, carrot and tomato. There are N different vegetable sellers in a line. Each vegetable seller sells all three vegetable items, but at different prices. Rahul, obsessed by his nature to spend optimally, decided not to purchase same vegetable from adjacent shops. Also, Rahul will purchase exactly one type of vegetable item (only 1 kg) from one shop. Rahul wishes to spend minimum money buying vegetables using this strategy. Help Rahul determine the minimum money he will spend.
Input
First line indicates number of test cases T. Each test case in its first line contains N denoting the number of vegetable sellers in Vegetable Market. Then each of next N lines contains three space separated integers denoting cost of brinjal, carrot and tomato per kg with that particular vegetable seller.
Output
For each test case, output the minimum cost of shopping taking the mentioned conditions into account in a separate line.
Rahul想购买主要是茄子，胡萝卜和西红柿的蔬菜。 一排有N种不同的蔬菜卖家。 每个蔬菜卖家都以不同的价格出售所有三种蔬菜。
Rahul因其性质而痴迷于最佳消费，决定不从邻近的商店购买同样的蔬菜。
此外，Rahul将从一家商店购买一种蔬菜项目（仅1公斤）。 Rahul希望用这种策略花最少的钱购买蔬菜。 帮助Rahul确定他将花费的最低金额。
输入
第一行表示测试用例的数量T.第一行中的每个测试用例包含N，表示蔬菜市场中的蔬菜销售商数量。
接下来N行中的每一行包含三个空格分隔的整数，表示每公斤与特定蔬菜销售商的茄子，胡萝卜和番茄的成本。
产量
对于每个测试用例，在单独的行中输出考虑上述条件的最小购物成本。
Constraints:1 <= T <= 101 <= N <= 100000 Cost of each vegetable(brinjal/carrot/tomato) per kg does not exceed 10^4
Sample Input 1 
 1
3
1 50 50
50 50 50
1 50 50
Sample Output 1
 52
'''


def main():
    t=int(input())
    ans=[]
    for i in range(t):
        n=int(input())
        a=[]
        for i in range(n):
            l=list(map(int,input().split()))
            m=[]
            if i==0:
                m=l
            else:
                m=[min(a[i-1][2],a[i-1][1])+l[0],min(a[i-1][0],a[i-1][2])+l[1],min(a[i-1][0],a[i-1][1])+l[2]]
            a.append(m)
        ans.append(min(a[-1]))
    for i in ans:
        print(i)

if __name__=="__main__": main()