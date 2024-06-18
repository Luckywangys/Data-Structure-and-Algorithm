'''
描述
有 n个小组要排成一个队列，每个小组中有若干人。
当一个人来到队列时，如果队列中已经有了自己小组的成员，他就直接插队排在自己小组成员的后面，否则就站在队伍的最后面。
请你编写一个程序，模拟这种小组队列。
输入
第一行：小组数量 t (t<100)。
接下来 t 行，每行输入一个小组描述，表示这个小组的人的编号。
编号是 0 到 999999 范围内的整数，一个小组最多可包含 1000 个人。
最后，命令列表如下。 有三种不同的命令：
1、ENQUEUE x - 将编号是 x 的人插入队列，编号不重复；
2、DEQUEUE - 让整个队列的第一个人出队；
3、STOP - 测试用例结束
每个命令占一行，不超过50000行。
输出
对于每个 DEQUEUE 命令，输出出队的人的编号，每个编号占一行。
'''

#2200015507 王一粟
from collections import deque
t = int(input())
mydict = {}
for i in range(1,t+1):
    s = input().split()
    for element in s:
        mydict[element] = i
d = deque()
queue = [deque() for i in range(t+1)]
while True:
    s = input()
    if s == "STOP":
        break
    if s == "DEQUEUE":
        try:
            try:
                idx = d[0]
            except:
                continue
            num = queue[idx].popleft()
            print(num)
            if queue[idx] == deque():
                d.popleft()
        except:
            print(idx)
            d.popleft()
    else:
        t,num = s.split()
        try:
            idx = mydict[num]
            if queue[idx] == deque():
                queue[idx].append(num)
                d.append(idx)
            else:
                queue[idx].append(num)
        except:
            d.append(num)