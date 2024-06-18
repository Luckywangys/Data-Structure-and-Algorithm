'''
描述
给定两个字符串a和b,我们定义a*b为他们的连接。例如，如果a=”abc” 而b=”def”， 则a*b=”abcdef”。 如果我们将连接考虑成乘法，一个非负整数的乘方将用一种通常的方式定义：a^0=””(空字符串)，a^(n+1)=a*(a^n)。
输入
每一个测试样例是一行可打印的字符作为输入，用s表示。s的长度至少为1，且不会超过一百万。最后的测试样例后面将是一个点号作为一行。
输出
对于每一个s，你应该打印最大的n，使得存在一个a，让s=a^n
'''

#2200015507 王一粟
while True:
    s = input()
    if s == ".":
        break
    length = len(s)
    next = [0 for i in range(length)]
    j = 0
    for i in range(1,length):
        while j>0 and s[i] != s[j]:
            j = next[j-1]
        if s[i] == s[j]:
            j += 1
        next[i] = j
    base_length = len(s) - next[-1]
    if len(s)%base_length == 0:
        print(len(s)//base_length)
    else:
        print(1)