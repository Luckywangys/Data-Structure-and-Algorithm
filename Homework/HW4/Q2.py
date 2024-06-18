'''
描述
波兰表达式是一种把运算符前置的算术表达式，例如普通的表达式2 + 3的波兰表示法为+ 2 3。波兰表达式的优点是运算符之间不必有优先级关系，也不必用括号改变运算次序，例如(2 + 3) * 4的波兰表示法为* + 2 3 4。本题求解波兰表达式的值，其中运算符包括+ - * /四个。
输入
输入为一行，其中运算符和运算数之间都用空格分隔，运算数是浮点数。
输出
输出为一行，表达式的值。
可直接用printf("%f\n", v)输出表达式的值v。
'''

#2200015507 王一粟
s = reversed(input().split())
stack = []
cnt = 0
for element in s:
    if element not in "+-*/":
        stack.append(element)
    else:
        op1 = stack.pop()
        op2 = stack.pop()
        stack.append(str(eval(op1+element+op2)))
result = float(stack[0])
print(f"{result:.6f}")



