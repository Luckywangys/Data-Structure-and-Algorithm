'''
描述
世界上有许多宗教，你感兴趣的是你学校里的同学信仰多少种宗教。
你的学校有n名学生（0 < n <= 50000），你不太可能询问每个人的宗教信仰，因为他们不太愿意透露。但是当你同时找到2名学生，他们却愿意告诉你他们是否信仰同一宗教，你可以通过很多这样的询问估算学校里的宗教数目的上限。你可以认为每名学生只会信仰最多一种宗教。
输入
输入包括多组数据。
每组数据的第一行包括n和m，0 <= m <= n(n-1)/2，其后m行每行包括两个数字i和j，表示学生i和学生j信仰同一宗教，学生被标号为1至n。输入以一行 n = m = 0 作为结束。
输出
对于每组数据，先输出它的编号（从1开始），接着输出学生信仰的不同宗教的数目上限。
'''

#2200015507 王一粟
def find(k):
    if parent[k] != k:
        parent[k] = find(parent[k])
    return parent[k]
def disjoint(m,n):
    m_rep = find(m)
    n_rep = find(n)
    if m_rep != n_rep:
        if size[m_rep] < size[n_rep]:
            size[m_rep] = size[m_rep] + size[n_rep]
            parent[n_rep] = m_rep
        else:
            size[n_rep] = size[m_rep] + size[n_rep]
            parent[m_rep] = n_rep
cnt = 0
while True:
    n,m = [int(i) for i in input().split()]
    if n == 0 and m == 0:
        break
    cnt += 1
    parent = [i for i in range(n+1)]
    size = [1 for i in range(n+1)]
    for _ in range(m):
        a,b = [int(i) for i in input().split()]
        disjoint(a,b)
    result = len([i for i in range(1,n+1) if parent[i]==i])
    print(f"Case {cnt}: {result}")