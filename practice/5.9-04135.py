'''
描述
农夫约翰是一个精明的会计师。他意识到自己可能没有足够的钱来维持农场的运转了。他计算出并记录下了接下来 N (1 ≤ N ≤ 100,000) 天里每天需要的开销。
约翰打算为连续的M (1 ≤ M ≤ N) 个财政周期创建预算案，他把一个财政周期命名为fajo月。每个fajo月包含一天或连续的多天，每天被恰好包含在一个fajo月里。
约翰的目标是合理安排每个fajo月包含的天数，使得开销最多的fajo月的开销尽可能少。
输入
第一行包含两个整数N,M，用单个空格隔开。
接下来N行，每行包含一个1到10000之间的整数，按顺序给出接下来N天里每天的开销。
输出
一个整数，即最大月度开销的最小值。
'''
#2200015507 王一粟
def solution(mid):
    outcome = 0
    wait = 0
    for element in mylist:
        if wait + element > mid:
            outcome += 1
            wait = element
        else:
            wait += element
    if wait != 0:
        outcome += 1
    return outcome <= m
n,m = [int(i) for i in input().split()]
max_num = 0
total = 0
mylist = []
for _ in range(n):
    num = int(input())
    max_num = max(max_num,num)
    mylist.append(num)
    total += num
start = max_num - 1
end = total
mid = (start+end)//2
while mid > start:
    if solution(mid):
        end = mid
        mid = (start+end)//2
    else:
        start = mid
        mid = (start+end)//2
print(end)