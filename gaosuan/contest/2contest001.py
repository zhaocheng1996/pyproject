n = int(input())
if(n>=0&n<=70):
  for i in range(0,n):
    array = input()
    array_tmp = array.strip(" ").split(" ")
    list1=[]
    list2=[]
    list3=[]
    for item in array_tmp:
        list1.append(int(item))
        list2.append((int(item)))
        list3.append((int(item)))

    # print(list1)
    # print(list2)
    num = (pow(list1[0],list1[1]))%list1[2]
    print(num)

