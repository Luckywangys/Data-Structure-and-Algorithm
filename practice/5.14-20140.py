'''
描述
常凯申同学发现自己今日化学论文字数抄上限了，决定采取如下的压缩方法萌混过关：
把连续的x个字符串s记为[xs]。(1 <= x <= 100)
但这样的方法当然骗不过lwh老师啦。老师非常生气，但出于好奇，还是想看一看常凯申同学写了什么。
请你帮老师还原出原始的论文。
输入
仅一行，由小写英文字母、数字和[]组成的字符串（其中不含空格）
输出
一行，原始的字符串。
'''

#2200015507 王一粟
s = input()
stack = []
num = ""
num_stack = []
for element in s:
    if element in "1234567890":
        num += element
        continue
    if num != "":
        num_stack.append(int(num))
        num = ""
    if element == "]":
        result = ""
        while stack:
            i = stack.pop()
            if i == "[":
                break
            result = i+result
        result = result*num_stack.pop()
        stack.extend(list(result))
    else:
        stack.append(element)
print("".join(stack))