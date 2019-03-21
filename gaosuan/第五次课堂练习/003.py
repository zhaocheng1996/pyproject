'''
时间与收益
Description
Given a set of n jobs where each job i has a deadline and profit associated to it. Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit if and only if the job is completed by its deadline. The task is to find the maximum profit and the number of jobs done.
给定一组n个工作，每个工作我都有截止日期和利润。每个作业需要1个单位的时间才能完成，一次只能安排一个作业。当且仅当工作在截止日期前完成时，我们才能获得利润。任务是找到最大的利润和完成的工作数量。
Input
The first line of input contains an integer T denoting the number of test cases.Each test case consist of an integer N denoting the number of jobs and the next line consist of Job id, Deadline and the Profit associated to that Job.
Constraints:1<=T<=100，1<=N<=100，1<=Deadline<=100，1<=Profit<=500
第一行输入包含一个整数T，表示测试用例的数量。每个测试用例包含一个表示作业数量的整数N，下一行包括作业ID，截止日期和与该作业相关的利润。
约束：1 <= T <= 100,1 <= N <= 100,1 <=截止<= 100,1 <=利润<= 500
Output
Output the number of jobs done and the maximum profit.
输出完成的工作数和最大利润。
Sample Input 1 
2
4
1 4 20 2 1 10 3 1 40 4 1 30
5
1 2 100 2 1 19 3 2 27 4 1 25 5 1 15
Sample Output 1
2 60
2 127
'''
def greed(jobs):
    time = jobs[1::3];#从下标一开始，每次跳3个
    value = jobs[2::3];
    tasks = 0
    total = 0

    for i in range(max(time), 0 ,-1):
        max_val = -1
        index = -1
        for j in range(len(time)):
            if time[j]>=i and value[j]>=max_val:
                max_val = value[j]
                index = j
        if max_val > 0:
            total += max_val;
            tasks += 1;
            value.pop(index)
            time.pop(index)
    print(tasks, total)

# jobs = [1,4,20,2,1,10,3,1,40,4,1,30]
# greed(jobs)

def main():
    T = int(input())
    for i in range(T):
        n = int(input())
        j = [int(x) for x in input().split()]
        greed(j)

if __name__ == '__main__':
   main();


