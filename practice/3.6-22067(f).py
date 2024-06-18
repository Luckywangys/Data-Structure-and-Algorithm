'''
描述
小明有很多猪，他喜欢玩叠猪游戏，就是将猪一头头叠起来。猪叠上去后，还可以把顶上的猪拿下来。小明知道每头猪的重量，而且他还随时想知道叠在那里的猪最轻的是多少斤。
输入
有三种输入
1)push n
n是整数(0<=0 <=20000)，表示叠上一头重量是n斤的新猪
2)pop
表示将猪堆顶的猪赶走。如果猪堆没猪，就啥也不干
3)min
表示问现在猪堆里最轻的猪多重。如果猪堆没猪，就啥也不干
输入总数不超过100000条
输出
对每个min输入，输出答案。如果猪堆没猪，就啥也不干
'''
#2200015507 王一粟
from collections import deque
stack = deque()
minnum = -1
mylist = []
while True:
    try:
        operate = input()
        if operate == "pop":
            if stack != deque():
                element = stack.pop()
                if element == minnum:
                    if stack != deque():
                        minnum = mylist.pop()
                    else:
                        minnum = -1
        elif operate == "min":
            if stack != deque():
                print(minnum)
        else:
            noi,yei = operate.split()
            pushnum = int(yei)
            if minnum == -1:
                minnum = pushnum
            else:
                if pushnum <= minnum:
                    mylist.append(minnum)
                    minnum = pushnum
            stack.append(pushnum)
    except:
        break

