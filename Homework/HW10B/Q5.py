'''
描述
老王喜欢喝冰阔落。
初始时刻，桌面上有n杯阔落，编号为1到n。老王总想把其中一杯阔落倒到另一杯中，这样他一次性就能喝很多很多阔落，假设杯子的容量是足够大的。
有m 次操作，每次操作包含两个整数x与y。
若原始编号为x 的阔落与原始编号为y的阔落已经在同一杯，请输出"Yes"；否则，我们将原始编号为y 所在杯子的所有阔落，倒往原始编号为x 所在的杯子，并输出"No"。
最后，老王想知道哪些杯子有冰阔落。
输入
有多组测试数据，少于 5 组。
每组测试数据，第一行两个整数 n, m (n, m<=50000)。接下来 m 行，每行两个整数 x, y (1<=x, y<=n)。
输出
每组测试数据，前 m 行输出 "Yes" 或者 "No"。
第 m+1 行输出一个整数，表示有阔落的杯子数量。
第 m+2 行有若干个整数，从小到大输出这些杯子的编号。
'''

#2200015507 王一粟
def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
while True:
    try:
        n,m = [int(i) for i in input().split()]
        parent = [i for i in range(n)]
        for i in range(m):
            x,y = [int(i)-1 for i in input().split()]
            x_represent,y_represent = find(x),find(y)
            if x_represent == y_represent:
                print("Yes")
            else:
                print("No")
                parent[y_represent] = parent[x_represent]
        result = [i+1 for i in range(n) if i == find(i)]
        print(len(result))
        print(" ".join(str(i) for i in result))
    except:
        break