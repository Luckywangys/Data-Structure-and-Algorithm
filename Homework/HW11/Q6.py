'''
描述
奶牛在熊大妈的带领下排成了一条直队。显然，不同的奶牛身高不一定相同……
现在，奶牛们想知道，如果找出一些连续的奶牛，要求最左边的奶牛 A 是最矮的，最右边的 B 是最高的，且 B 高于 A 奶牛。中间如果存在奶牛，则身高不能和 A,B 奶牛相同。问这样的奶牛最多会有多少头？
从左到右给出奶牛的身高，请告诉它们符合条件的最多的奶牛数（答案可能是 0,2，但不会是 1）。
输入
第一行一个正整数 N，表示奶牛的头数。(2<=N<=10000)
接下来 N 行，每行一个正整数，从上到下表示从左到右奶牛的身高 hi (1<=hi<=50000000) 。
输出
一行一个整数，表示最多奶牛数。
'''

#2200015507 王一粟
n = int(input())
mylist = []
max_num = 0
for i in range(n):
    t = int(input())
    mylist.append(t)
max_list = sorted(mylist)
total_max = max_list[-1]
stack = [mylist[0]]
if mylist[0] == total_max:
    max_list.pop()
    total_max = max_list[-1]
result = 0
max_num = stack[0]
cnt = 1
for _ in range(1,n):
    num = mylist[_]
    if num == total_max:
        result = max(result,cnt+1)
        stack = [num]
        max_list.pop()
        total_max = max_list[-1]
        max_num = num
        continue
    if num <= stack[0]:
        stack = [num]
        max_num = num
        cnt = 1
        continue
    stack.append(num)
    cnt += 1
    if num > max_num:
        max_num = num
        result = max(result,cnt)
if result != 1:
    print(result)
else:
    print(0)