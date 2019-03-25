'''
选择排序：第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；
以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕
时间复杂度：O(n²),需要进行的比较次数为第一轮 n-1，n-2....1, 总的比较次数为 n*(n-1)/2
空间复杂度：O(1)
稳定性：不稳定
'''

def select_sort(myList):
    # 获取list的长度
    length = len(myList)
    # 一共进行多少轮比较
    for i in range(0, length - 1):
        # 默认设置最小值得index为当前值
        smallest = i
        # 用当先最小index的值分别与后面的值进行比较,以便获取最小index
        for j in range(i + 1, length):
            # 如果找到比当前值小的index,则进行两值交换
            if myList[j] < myList[smallest]:
               myList[j],myList[smallest] = myList[smallest],myList[j]
        # 打印每一轮比较好的列表
        print("Round ", i, ": ", myList)

ilist = select_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
print(ilist)





