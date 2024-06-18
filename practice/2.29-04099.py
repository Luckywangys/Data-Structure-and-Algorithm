'''
描述
队列和栈是两种重要的数据结构，它们具有push k和pop操作。push k是将数字k加入到队列或栈中，pop则是从队列和栈取一个数出来。队列和栈的区别在于取数的位置是不同的。
队列是先进先出的：把队列看成横向的一个通道，则push k是将k放到队列的最右边，而pop则是从队列的最左边取出一个数。
栈是后进先出的：把栈也看成横向的一个通道，则push k是将k放到栈的最右边，而pop也是从栈的最右边取出一个数。
假设队列和栈当前从左至右都含有1和2两个数，则执行push 5和pop操作示例图如下：
          push 5          pop
队列 1 2  ------->  1 2 5 ------>  2 5
          push 5          pop

栈   1 2  ------->  1 2 5 ------>  1 2
现在，假设队列和栈都是空的。给定一系列push k和pop操作之后，输出队列和栈中存的数字。若队列或栈已经空了，仍然接收到pop操作，则输出error。
输入
第一行为m，表示有m组测试输入，m<100。
每组第一行为n，表示下列有n行push k或pop操作。（n<150）
接下来n行，每行是push k或者pop，其中k是一个整数。
（输入保证同时在队列或栈中的数不会超过100个）
输出
对每组测试数据输出两行，正常情况下，第一行是队列中从左到右存的数字，第二行是栈中从左到右存的数字。若操作过程中队列或栈已空仍然收到pop，则输出error。输出应该共2*m行。
'''

#2200015507 王一粟
m = int(input())
for _ in range(m):
    n = int(input())
    queue = []
    stack = []
    cnt = 0
    for i in range(n):
        operation = input()
        if cnt == 1:
            continue
        else:
            if operation == "pop":
                if len(queue) == 0:
                    cnt = 1
                    print("error")
                    print("error")
                    continue
                else:
                    del queue[0]
                    stack.pop()
            else:
                operate,value = operation.split()
                value = int(value)
                queue.append(value)
                stack.append(value)
    if cnt == 0:
        print(" ".join(str(k) for k in queue))
        print(" ".join(str(k) for k in stack))