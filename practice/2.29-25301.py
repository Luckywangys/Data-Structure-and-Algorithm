'''
描述
在一个有210人的大班级中，存在两个人生日相同的概率非常大，现给出每个学生的学号，出生日期。试找出所有生日相同的学生。
输入
第一行为整数n，表示有n个学生，n < 100 。
此后每行包含一个字符串和两个整数，分别表示学生的学号（字符串长度小于10）和出生月（1 <= m <= 12）日（1 <= d <= 31）。
学号、月、日之间用一个空格凤娥。
输出
对每组生日相同的学生，输出一行，
其中前两个数字表示月和日，后面跟着所有在当天出生的学生的学号，数字、学号之间都用一个空格分隔。
对所有的输出，要求按照日期从前到后的顺序输出。
对生日相同的学号，按输入的顺序输出。
'''

#2200015507 王一粟
n = int(input())
mydict = {}
for i in range(n):
    id,m,d = input().split()
    m = int(m)
    d = int(d)
    if (m,d) in mydict:
        mydict[(m,d)].append(id)
    else:
        mydict[(m,d)] = [id]
mylist = sorted(mydict.items(),key = lambda x:x[0])
for i in mylist:
    if len(i[1])>1:
        print(i[0][0], i[0][1], " ".join(k for k in i[1]))