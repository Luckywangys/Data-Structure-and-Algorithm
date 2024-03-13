'''
描述
n 个小孩围坐成一圈，并按顺时针编号为1,2,…,n，从编号为 p 的小孩顺时针依次报数，由1报到m ，当报到 m 时，该小孩从圈中出去，然后下一个再从1报数，当报到 m 时再出去。如此反复，直至所有的小孩都从圈中出去。请按出去的先后顺序输出小孩的编号。
输入
每行是用空格分开的三个整数，第一个是n,第二个是p,第三个是m (0 < m,n < 300)。最后一行是:
0 0 0
输出
按出圈的顺序输出编号，编号之间以逗号间隔。
'''

#2200015507 王一粟
from collections import deque
while True:
    n,p,m = [int(i) for i in input().split()]
    if n == 0:
        break
    myqueue = deque()
    for i in range(p,p+n):
        if i<=n:
            myqueue.append(i)
        else:
            myqueue.append(i-n)
    resultlist = []
    while len(resultlist)<n:
        for k in range(m-1):
            myqueue.append(myqueue.popleft())
        resultlist.append(myqueue.popleft())
    print(",".join(str(i) for i in resultlist))
