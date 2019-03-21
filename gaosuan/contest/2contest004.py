n = int(input())
result=[]
for i in range(0,n):
    count=0
    arr = input()
    list=[]
    arr_tmp = arr.strip(" ").split(" ")
    for item in arr_tmp:
        list.append(int(item))
        number=list[0]
        #print(number)
        number1=number**0.5
        if(number1%1==0.0):
           for i in range(0,number):
               div=number%(i+1)
               if(div==0):
                 count+=1
    #print(count)
    if(count==9):
        result.append(1)
    else:
        result.append(0)
for item in result:
    print(item)
