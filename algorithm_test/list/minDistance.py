'''
给定一个数组，数组中含有重复元素，给定两个数字 numl 和 nurn2，
求这两个数字在数组中出现的位置的最小距离。
：蛮力法 主要思路为：对数组进行双重遍历，外层循环遍历查找 numl，只要遍历到 numl ，
内层 循环对数组从头开始遍历找 num2，每当遍历到 num2，就计算它们的距离 dist。
当遍历结束后 最小的 dist 值就是它们最小的距离。
'''
def minDistance(arr,num1,num2):
    mindist=100
    dist=0
    i = 0
    while i<len(arr):
        if arr[i] == num1:
            j = 0
            while j<len(arr):
                if arr[j]==num2:
                    dist = abs(i-j)
                    if dist<mindist:
                        mindist=dist
                j+=1
        i+=1
    return mindist

arr = [4,5,6,4,7,4,6,4,7,8,5,6,4,3,10,8]
print(minDistance(arr,4,8))

'''
：动态规划 
可以采用动态规划的方 法把每次遍历的结果都记录下来从而减少遍历次数。
具体实现思路为：遍历数组，会遇到以 下两种情况： 
1.当遇到numl时，记录下numl值对应的数组下标的位置lastPosl通过求lastPosl
与上次遍历到num2下标的位置的值 lastPos2 的差可以求出最近一次遍历到的 numl 与 num2 的距离。 
当遇到num2时，同样记录下它在数组中下标的位置lastPos2然后通过求lastPos2 
与上次遍历到numl的下标值lastPosl，求出最近一次遍历到的numl与num2的距离。 
假设给定数组为：［4,5,6,4,7,4,6,4,7,8,5,6,4,3,10,8],num1=4,num2=8。
根据以上方法，执行过程如下：
1.在遍历的时候首先会遍历到4，下标为 lastPosl=O，由于此时还没有遍历到 num2，
因此没必要计算numl与num2的最小距离； 
2）接着往下遍历，又遍历到num1=4，更新lastPos1=3;
3）接着往下遍历，又遍历到num1=4，更新lastPos1 =7; 
接着往下遍历，又遍历到num2=8，更新lastPos2=9；
此时由于前面已经遍历到过numl，因此，可以求出当前numl与num2的最小距离为 
lastPos2- lastPosl=2;
5）接着往下遍历，又遍历到num2=8，更新lastPos2=15：
此时由于前面已经遍历到过numl,因此,可以求出当前numl与num2的最小距离为
lastPos2-lastPos1=8：由于8>2，所以numl与num2 的最小距离为 2。 
'''

def minDistance2(arr,num1,num2):
    lastPos1 = -1#上一次遍历到num1的位置
    lastPos2 = -1
    minDist = 100
    i = 0
    while i<len(arr):
        if arr[i]==num1:
            lastPos1=i
            if lastPos2>=0:
                minDist = min(minDist,abs(lastPos2-lastPos1))
        if arr[i]==num2:
            lastPos2=i
            if lastPos1>=0:
                minDist = min(minDist,abs(lastPos1-lastPos2))
        i+=1
    return minDist

arr = [4,5,6,4,7,4,6,4,7,8,5,6,4,3,10,8]
print(minDistance2(arr,4,8))