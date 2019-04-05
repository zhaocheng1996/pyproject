'''
一个有n个元素的数组，这n个元素既可以是正数也可以是负数，数组中连续的一个或多个元素可以组成一个连续的子数组，
一个数组可能有多个这种连续的子数组，求子数组和 的最大值。
例如：对于数组［1, -2, 4, 8, -4, 7,一l，一5］而言，其最大和的子数组为［4, 8, -4, 7］， 最大值为 15。

最大和连续子数组一定有如下几个特点：
1、第一个不为负数
2、如果前面数的累加值加上当前数后的值会比当前数小，说明累计值对整体和是有害的；如果前面数的累加值加上当前数后的值比当前数大或者等于，则说明累计值对整体和是有益的。
步骤：
1、定义两个变量，一个用来存储之前的累加值，一个用来存储当前的最大和。遍历数组中的每个元素，假设遍历到第i个数时：
①如果前面的累加值为负数或者等于0，那对累加值清0重新累加，把当前的第i个数的值赋给累加值。
②如果前面的累加值为整数，那么继续累加，即之前的累加值加上当前第i个数的值作为新的累加值。
2、判断累加值是否大于最大值：如果大于最大值，则最大和更新；否则，继续保留之前的最大和
'''

def function(lists):
    max_sum = lists[0]
    pre_sum = 0
    for i in lists:
        if pre_sum < 0:
            pre_sum = i
        else:
            pre_sum += i
        if pre_sum > max_sum:
            max_sum = pre_sum
    return max_sum
arr=[1,-2,4,8,-4,7,-1,-5]
print(function(arr))

