'''
描述
剧组为了整演员，提供给他们的提词本是经过加工的
提词本内容由英文字母跟括号组成，而且括号必定合法，左括号一定有对应的右括号
演员必须从最里层开始翻转括号内的字母
例如(dcba) 要翻转成abcd
最终演员所念的台词不能含有括号
请输出演员应该念出来的台词
输入
一个字串s
输出
一个字串s2
'''

#2200015507 王一粟
s = input()
stack = []
for char in s:
    if char == "(":
        stack.append(char)
    elif char == ")":
        mylist = []
        while stack[-1] != "(":
            mylist.append(stack.pop())
        stack.pop()
        stack.extend(mylist)
    else:
        stack.append(char)
print("".join(stack))