'''
给定一个带整数的数组。
两个非重叠的子阵列A和B，这|SUM(A) - SUM(B)|是最大的。
返回最大的差异。
例1：
Input:[1, 2, -3, 1]
Output:6
Explanation:
The subarray are [1,2] and [-3].So the answer is 6.
例2：
Input:[0,-1]
Output:1
Explanation:
The subarray are [0] and [-1].So the answer is 1.
'''
'''
思路是类似的，先从左到右遍历数组，保存遍历到每个元素的当前的最大和最小连续子数组的值。然后从右遍历数组，记录同样的最大和最小连续子数组的值；遍历数组比较每种组合的左右最大连续子数组的差值，返回最大的值。
也就是说我们需要记录四个数组：leftmax、leftmin、rightmax、rightmin。
最后得到两个差值：
differ1=左边最大减去右边最小
differ2=右边最大减去左边最小
比较二者，比较高的就是最后的答案。
'''

def maxDiffsubArrays(nums):
    if(len(nums)==2):
        return abs(nums[0]-nums[1])
    # dpleftmax、dprightmax数组记录每个位置结尾的子数组最大和
    # dpleftmin、dprightmin数组记录每个位置结尾的子数组最小和
    # dpleftmax从左到右遍历
    dpleftmax = [0 for i in range(len(nums))]
    maxp = -99
    sum = 0
    for i in range(0,len(nums)):
        if(sum<0):
            sum = nums[i]
        else:
            sum += nums[i]
        maxp = max(maxp,sum)
        dpleftmax[i] = maxp
    print(dpleftmax)#([1, 3, 3, 3])

    #dprightmax记录从右到左遍历子数组的最大和
    dprightmax = [0 for i in range(len(nums))]
    maxp = -99
    sum = 0
    for i in range(len(nums)-1,-1,-1):
        if(sum<0):
            sum = nums[i]
        else:
            sum+=nums[i]
    maxp = max(maxp,sum)
    dprightmax[i] = maxp
    print(dprightmax)

    #做左边起最小的和
    dpleftmin = [0 for i in range(len(nums))]
    minp = 99
    sum = 0
    for i in range(len(nums)):
        if(sum>0):
            sum=nums[i]
        else:
            sum += nums[i]
        minp = min(minp,sum)
        dpleftmin[i] = minp
    print(dpleftmin)

    # 做右边起最小的和
    dprightmin = [0 for i in range(len(nums))]
    minp = 99
    sum = 0
    for i in range(len(nums)-1,-1,-1):
        if (sum > 0):
            sum = nums[i]
        else:
            sum += nums[i]
        minp = min(minp, sum)
        dprightmin[i] = minp
    print(dprightmin)

    differ1 = max(dpleftmax)-min(dprightmin)
    differ2 = max(dprightmax)-min(dpleftmin)
    sum = max(differ1,differ2)
    print(sum)

maxDiffsubArrays([1, 2, -3, 1])


