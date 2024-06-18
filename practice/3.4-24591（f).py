'''
描述
中序表达式是运算符放在两个数中间的表达式。乘、除运算优先级高于加减。可以用"()"来提升优先级 --- 就是小学生写的四则算术运算表达式。中序表达式可用如下方式递归定义：
1）一个数是一个中序表达式。该表达式的值就是数的值。
2) 若a是中序表达式，则"(a)"也是中序表达式(引号不算)，值为a的值。
3) 若a,b是中序表达式，c是运算符，则"acb"是中序表达式。"acb"的值是对a和b做c运算的结果，且a是左操作数，b是右操作数。
输入一个中序表达式，要求转换成一个后序表达式输出。
输入
第一行是整数n(n<100)。接下来n行，每行一个中序表达式，数和运算符之间没有空格，长度不超过700。
输出
对每个中序表达式，输出转成后序表达式后的结果。后序表达式的数之间、数和运算符之间用一个空格分开。
'''

#2200015507 王一粟
def post(expression):
    stack = []
    postexpress = []
    num = ""
    for char in expression:
        if char in "1234567890" or char in ".":
            num = num + char
            continue
        if num != "":
            postexpress.append(num)
            num = ""
        if char == "(":
            stack.append(char)
        elif char == ")":
            while stack:
                if stack[-1] == "(":
                    del stack[-1]
                    break
                else:
                    postexpress.append(stack.pop())
        elif char in "+-":
            while stack and stack[-1] in "+-*/":
                postexpress.append(stack.pop())
            stack.append(char)
        else:
            while stack and stack[-1] in "*/":
                postexpress.append(stack.pop())
            stack.append(char)
    if num != "":
        postexpress.append(num)
    while stack != []:
        postexpress.append(stack.pop())
    return " ".join(postexpress)
n = int(input())
for i in range(n):
    s = input()
    print(post(s))