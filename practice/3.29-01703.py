'''
描述
一个城市中有两个犯罪团伙A和B，你需要帮助警察判断任意两起案件是否是同一个犯罪团伙所为，警察所获得的信息是有限的。假设现在有N起案件（N<=100000），编号为1到N，每起案件由团伙A或团伙B所为。你将按时间顺序获得M条信息（M<=100000），这些信息分为两类：
1. D [a] [b]
其中[a]和[b]表示两起案件的编号，这条信息表明它们属于不同的团伙所为
2. A [a] [b]
其中[a]和[b]表示两起案件的编号，这条信息需要你回答[a]和[b]是否是同一个团伙所为
注意你获得信息的时间是有先后顺序的，在回答的时候只能根据已经接收到的信息做出判断。
输入
第一行是测试数据的数量T（1<=T<=20）。
每组测试数据的第一行包括两个数N和M，分别表示案件的数量和信息的数量，其后M行表示按时间顺序收到的M条信息。
输出
对于每条需要回答的信息，你需要输出一行答案。如果是同一个团伙所为，回答"In the same gang."，如果不是，回答"In different gangs."，如果不确定，回答”Not sure yet."。
'''

#2200015507 王一粟
def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]
def disjoint(a,b):
    repa = find(a)
    repb = find(b)
    if repa != repb:
        if rank[repa] < rank[repb]:
            parent[repa] = repb
            rank[repb] = rank[repa] + 1
        else:
            parent[repb] = repa
            rank[repa] = rank[repb] + 1
t = int(input())
for _ in range(t):
    n,m = [int(i) for i in input().split()]
    parent = [i for i in range(2*n+1)]
    rank = [1 for i in range(2*n+1)]
    for i in range(m):
        kind,num1,num2 = input().split()
        num1 = int(num1)
        num2 = int(num2)
        if kind == "D":
            disjoint(num1,n+num2)
            disjoint(n+num1,num2)
        if kind == "A":
            if find(num1) == find(num2):
                print("In the same gang.")
            elif find(num1) == find(num2+n):
                print("In different gangs.")
            else:
                print("Not sure yet.")