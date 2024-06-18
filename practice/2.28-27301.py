'''
描述
Alice 和 Bob 打算给花园里的 n 株植物浇水。植物排成一行，从左到右进行标记，编号从 0 到 n - 1，每一株植物都需要浇特定量的水。Alice 和 Bob 每人有一个水罐，容量分别为 a 和 b，最初是满的。他们按下面描述的方式完成浇水：
每株植物都可以由 Alice 或者 Bob 来浇水。Alice 按从左到右的顺序从植物 0 开始浇水；Bob 按从右到左的顺序从植物 n - 1 开始浇水。二人同时开始。
不管植物需要多少水，浇水所耗费的时间都是一样的。
如果没有足够的水完全浇灌下一株植物，他 / 她会立即重新灌满浇水罐，再给下一株植物浇水。不能提前重新灌满水罐。保证 a 和 b 均大于任意一株植物需要浇水的量。
如果 Alice 和 Bob 到达同一株植物，那么当前水罐中水更多的人会给这株植物浇水。如果他俩水量相同，那么 Alice 会给这株植物浇水。
请你写一个程序，计算两人浇灌所有植物过程中重新灌满水罐的总次数。
输入
第一行为三个正整数 n, a, b，分别表示植物个数，Alice 和 Bob 的水罐容量。n <= 100
第二行为 n 个空格分隔的正整数，表示每株植物需要的浇水量。
输出
一个正整数，表示 Alice 和 Bob完成浇水所需要重新灌满水罐的总次数。
'''

#2200015507 王一粟
n,a,b = [int(i) for i in input().split()]
mylist = [int(i) for i in input().split()]
cnta = a
cntb = b
repeats = 0
half = n//2
for i in range(0,half):
    if cnta<mylist[i]:
        cnta = a
        repeats+=1
    cnta = cnta - mylist[i]
for i in range(n-1,n-1-half,-1):
    if cntb<mylist[i]:
        cntb = b
        repeats+=1
    cntb = cntb-mylist[i]
if n%2 != 0:
    if max(cnta,cntb)<mylist[half]:
        repeats += 1
print(repeats)