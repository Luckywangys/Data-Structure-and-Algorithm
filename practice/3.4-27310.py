'''
描述
为了提高她的词汇量，奶牛 Bessie 拿来了一套共四块积木，每块积木都是一个正方体，六面各写着一个字母。她正在将积木排成一排，使积木顶部的字母拼出单词，以此来学习拼写。
给定 Bessie 四块积木上的字母，以及她想要拼写的单词列表，请判断她可以使用积木成功拼写列表中的哪些单词。
输入
输入的第一行包含 N（1 ≤ N ≤ 10），为 Bessie 想要拼写的单词数。以下四行，每行包含一个包含六个大写字母的字符串，表示 Bessie 的一块积木六面上的字母。以下 N 行包含 Bessie 想要拼写的 N 个单词。每一个均由 1 到 4 个大写字母组成。
输出
对于 Bessie 的列表中的每一个单词，如果她可以拼写这个单词则输出 YES，否则输出 NO
'''

#2200015507 王一粟
n = int(input())
cube1 = list(input())
cube2 = list(input())
cube3 = list(input())
cube4 = list(input())
mylist = []
for i in cube1:
    for j in cube2:
        for k in cube3:
            for p in cube4:
                alist = sorted([i,j,k,p])
                astring = "".join(alist)
                mylist.append(astring)
                bstring = astring[0]+astring[2]+astring[3]
                cstring = astring[0]+astring[2]
                dstring = astring[0]+astring[3]
                estring = astring[1]+astring[3]
                mylist.append(bstring)
                mylist.append(cstring)
                mylist.append(dstring)
                mylist.append(estring)
for i in range(n):
    s = sorted(list(input()))
    astring = "".join(s)
    cnt = 0
    for j in mylist:
        if astring in j:
            print("YES")
            cnt = 1
            break
    if cnt == 0:
        print("NO")