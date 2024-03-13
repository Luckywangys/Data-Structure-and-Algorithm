'''
描述
给定一个由大小写字母和数字构成的，没有重复字符的长度不超过62的字符串x，现在要将该字符串的字符依次压入栈中，然后再全部弹出。
要求左边的字符一定比右边的字符先入栈，出栈顺序无要求。
再给定若干字符串，对每个字符串，判断其是否是可能的x中的字符的出栈序列。
输入
第一行是原始字符串x
后面有若干行(不超过50行)，每行一个字符串，所有字符串长度不超过100
输出
对除第一行以外的每个字符串，判断其是否是可能的出栈序列。如果是，输出"YES"，否则，输出"NO"
'''
#2200015507 王一粟
myorigin = list(input())
while True:
    try:
        stack = []
        origin = myorigin.copy()
        check = list(input())
        if len(origin) != len(check):
            print("NO")
            continue
        for char in origin:
            if char != check[0]:
                stack.append(char)
            else:
                del check[0]
                while stack and stack[-1] == check[0]:
                    del check[0]
                    stack.pop()
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")
    except:
        break