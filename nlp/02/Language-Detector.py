in_f = open('data.csv')
lines = in_f.readlines()
for line in lines:
    print(line.strip())
    print(line.strip()[:-3])
    #print(line.strip()[-2:])
in_f.close()
dataset = [(line.strip()[:-3], line.strip()[-2:]) for line in lines]

#print(dataset[:5])

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[:-3],L[-2:])
# L = list(range(100))
# print(L)
# print(L[:-3])
#[-2:0]取最后两个，[:-3]取除了最后三个



