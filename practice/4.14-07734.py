'''
描述
Hopper 博士正在研究一种罕见种类的虫子的性行为。他假定虫子只表现为两种性别，并且虫子只与异性进行交互。在他的实验中，不同的虫子个体和虫子的交互行为很容易区分开来，因为这些虫子的背上都被标记有一些标号。
现在给定一系列的虫子的交互，现在让你判断实验的结果是否验证了他的关于没有同性恋的虫子的假设或者是否存在一些虫子之间的交互证明假设是错的。
输入
输入的第一行包含实验的组数。每组实验数据第一行是虫子的个数（至少1个，最多2000个) 和交互的次数 (最多1000000次) ，以空格间隔. 在下面的几行中,每次交互通过给出交互的两个虫子的标号来表示，标号之间以空格间隔。已知虫子从1开始连续编号。
输出
每组测试数据的输出为2行，第一行包含 "Scenario #i:", 其中 i 是实验数据组数的标号，从1开始,第二行为 "No suspicious bugs found!" 如果实验结果和博士的假设相符,或 "Suspicious bugs found!" 如果Hopper的博士的假设是错误的
'''

#2200015507 王一粟
def find(x):
    if note[x] == x:
        return x
    else:
        note[x] = find(note[x])
        return note[x]
def disjoint(a,b):
    rep_a,rep_b = find(a),find(b)
    if rep_a == rep_b:
        return
    if rank[rep_a] < rank[rep_b]:
        note[rep_a] = rep_b
    elif rank[rep_a] > rank[rep_b]:
        note[rep_b] = rep_a
    else:
        note[rep_a] = rep_b
        rank[rep_b] += 1
for _ in range(int(input())):
    n,times = [int(i) for i in input().split()]
    note = [int(i) for i in range(2*n+1)]
    rank = [0]*(2*n+1)
    cnt = 0
    for i in range(times):
        love1,love2 = [int(i) for i in input().split()]
        if cnt == 1:
            continue
        if find(love1) == find(love2) or find(love1+n) == find(love2+n):
            cnt = 1
            continue
        disjoint(love1+n,love2)
        disjoint(love2+n,love1)
    if _ != 0:
        print()
    print(f"Scenario #{_+1}:")
    if cnt == 0:
        print("No suspicious bugs found!")
    else:
        print("Suspicious bugs found!")

