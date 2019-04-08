graph = {
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]
}

def BFS(graph,start):
    queue = []
    queue.append(start)
    seen = set()#储存已经被看到过的结点
    seen.add(start)
    while (len(queue)>0):
        vertax = queue.pop(0)
        #接着把这个点的所有临接点放到队列中
        nodes = graph[vertax]#vertax的所有临接点是nodes
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertax,end=' ')#A B C D E F
BFS(graph,"A")
print()
def DFS(grapg,start):
    stack = []
    stack.append(start)
    seen = set()
    seen.add(start)
    while len(stack)>0:
        vertax = stack.pop()#弹出的时候弹出最后一个元素
        nodes = graph[vertax]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertax,end=' ')

DFS(graph,'A')
print()
#找到最短路径
def BFS(graph,start):
    queue = []
    queue.append(start)
    seen = set()#储存已经被看到过的结点
    seen.add(start)
    parent = {start:None}

    while (len(queue)>0):
        vertax = queue.pop(0)
        #接着把这个点的所有临接点放到队列中
        nodes = graph[vertax]#vertax的所有临接点是nodes
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertax
        print(vertax,end=' ')#A B C D E F
    print()
    return parent

parent = BFS(graph,'A')
#打印出每个点对应的前一个结点
for key in parent:
    print(key,parent[key])
#单独看某一个点的前驱
v = "B"
while v != None:
    print(v,end=' ')
    v = parent[v]
