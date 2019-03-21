'''
无限递归字符串查询
Description
Consider a string A = "12345". An infinite string s is built by performing infinite steps on A recursively. In i-th step, A is concatenated with ‘$’ i times followed by reverse of A. A=A|$...$|reverse(A), where | denotes concatenation.
Constraints:1<=Q<=10^5, 1<=POS<=10^12
Input
输入第一行为查询次数，后面为每次查询的具体字符位置。
Output
输出每一次查询位置上的字符。
Sample Input 1 
2
3
10
Sample Output 1
3
2
'''

q = int(input().strip())
arr = ['$', '1', '2', '3', '4', '5', '$', '5','4','3','2','1']
for _ in range(q):
   print(arr[int(input().strip()) % 12])


