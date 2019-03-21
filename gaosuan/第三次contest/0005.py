'''
牛的繁殖问题
Description
Cows in the FooLand city are interesting animals. One of their specialties is related to producing offsprings. A cow in FooLand produces its first calve (female calf) at the age of two years and proceeds to produce other calves (one female calf a year).
Now the farmer Harold wants to know how many animals would he have at the end of N years, if we assume that none of the calves die, given that initially, he has only one female calf?
explanation:At the end of 1 year, he will have only 1 cow, at the end of 2 years he will have 2 animals (one parent cow C1 and other baby calf B1 which is the offspring of cow C1).At the end of 3 years, he will have 3 animals (one parent cow C1 and 2 female calves B1 and B2, C1 is the parent of B1 and B2).At the end of 4 years, he will have 5 animals (one parent cow C1, 3 offsprings of C1 i.e. B1, B2, B3 and one offspring of B1).
FooLand市的奶牛是有趣的动物。他们的专长之一与生产子孙有关。FooLand的一头母牛在两岁时生产出它的第一只小牛（雌性小牛），并继续生产其他小牛（每年一只雌性小牛）。
如果我们假设没有一只小牛死了，那么农民哈罗德想要知道他在N年结束时会有多少只动物，因为最初，他只有一只雌性小牛？
Input
The first line contains a single integer T denoting the number of test cases. Each line of the test case contains a single integer N as described in the problem.
第一行包含一个整数T，表示测试用例的数量。 测试用例的每一行包含问题中描述的单个整数N.
Output
For each test case print in new line the number of animals expected at the end of N years modulo 10^9 + 7.
对于每个测试用例，在新行中打印预计在N年结束时的动物数量为10 ^ 9 + 7。
Sample Input 1 
2
2
4
Sample Output 1
2
5
'''
t=int(input())
for _ in range(t):
  n=int(input())
  cow=[1,1]
  for i in range(2,n+1):
     cow.append(cow[i-1]+cow[i-2])
     print(int(max(cow)))

