n=int(input())
result=[]
for i in range(0,n):
    num=int(input())
    array=input()
    array_tmp=array.strip(" ").split(" ")
    list1=[]
    list2=[]
    for item in array_tmp:
        list1.append(int(item))
        list2.append(int(item))
    sum=0

    print(list1)
    print(list2)

    list2.sort()
    for i in range(0,len(list1)):
        if list1[i]!=list2[i]:
            sum+=1
            index=list2.index(list1[i])#找出一个匹配项的索引位置
            t=list1[i]
            list1[i]=list1[index]
            list1[index]=t
    result.append(sum)
for item in result:
    print(item)



