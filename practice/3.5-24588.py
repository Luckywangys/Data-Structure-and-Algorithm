'''
输入
第一行是整数n(n<100)，接下来有n行，每行是一个后序表达式，长度不超过1000个字符
输出
对每个后序表达式，输出其值，保留小数点后面2位
'''

#2200015507 王一粟
n = int(input())
for _ in range(n):
    post = input().split()
    stack = []
    for element in post:
        if element in "+-*/":
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(str(eval(op1+element+op2)))
        else:
            stack.append(element)
    print(f"{float(stack[0]):.2f}")