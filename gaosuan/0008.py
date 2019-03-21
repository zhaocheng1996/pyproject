'''
有两个序列a，b，大小都为n，序列元素的值任意整数，无序；要求：通过交换啊a，b中的元素，使
[序列a元素的和]与[序列b元素的和]之间的差最小
input 输入为两行，分别为两个数组，每个值使用空格隔开
output 输出变化后的两个数组内元素和的差绝对值
sample input 100 99 98 1 2 3
1 2 3 4 5 40
sample out 96
'''


def get_MinDvalue(a,b):
    # combinations是一个生成器（迭代器），每次从a+b中取出n个数返回一个列表，并且会列举出所有种情况
    # 这个列表的和与sum(a+b)/2差值的绝对值的最小值就是题目要求的最小差值
    return min(combinations(a+b, len(a+b)/2), key=lambda x:abs(sum(x)-sum(a+b)/2))

def combinations(numbers, length, num=0, begin=0):
# nums用于表示当前以及取出了多个数字了
# begin用来表示迭代中for循环的起点序列
    for i in range(begin,len(numbers)):
        if num == length-1:
            yield [numbers[i]]
        for result in combinations(numbers, length, num+1, begin=i++1):
            yield [numbers[i]] + result

arr1 = [100,99,98,1,2,3]
arr2 = [1,2,3,4,5,40]
print(get_MinDvalue(arr1,arr2))


