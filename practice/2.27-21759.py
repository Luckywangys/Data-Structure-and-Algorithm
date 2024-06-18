'''
描述
古人云：“开卷有益”。但是，著名的社会学家小明认为内卷是有害的，并且他正在写一篇与P大内卷现状有关的论文，需要选取具有代表性的“卷王”们进行访谈。小明现在搞到了一份长长的成绩单，拜托你写个程序，帮他找出成绩单上的“卷王”们。

小明把“卷王”定义为：学过的课程数量大于等于x门，且课程得分平均分大于y的学生。

输入
第1行：三个用空格分隔的整数n，x，y，1 <= n <= 100000，x >= 0，0 <= y <= 100
第2~(n+1)行：每行有用空格分隔的两个字符串和一个整数，前两个字符串分别代表课程名和学生名，最后一个整数代表这个学生在此课程中取得的成绩。输入保证课程名和学生名只包含字母，且一个学生在一个课程中不会出现两次成绩。输入不保证任何顺序。

第n+2行：一个整数m，代表查询的个数，1 <= m <= 1000

第(n+3)~(n+m+2)行：每行是一个查询字符串，代表学生名，数据保证学生名一定在前面出现过。
输出
输出为m行，对于每个查询，如果这个学生是卷王，输出yes；如果不是卷王，输出no，注意，输出都是小写。
'''

#2200015507 王一粟
n,x,y =[int(i) for i in input().split()]
mydict = {}
for i in range(n):
    course,name,grade = input().split()
    grade = int(grade)
    if name in mydict:
        mydict[name].append(grade)
    else:
        mydict[name] = [grade]
m = int(input())
for i in range(m):
    name = input()
    mylist = mydict[name]
    if len(mylist)>=x and sum(mylist)/len(mylist)>y:
        print("yes")
    else:
        print("no")