'''
描述
某网站上中有某一天内用户访问的网页的记录，程序要统计出访问时长最多的网页。
输入的数据是这样的格式：网页 起始时间 结束时间，数据之间用空格分开。
index.html 10:25:00 10:25:06
study.html 10:25:45 10:26:01
index.html 10:26:00 10:29:03
teachers.html 10:59:01 11:01:03
每个网页的访问时间等于结束时间减起始时间（时间可化为秒数，方便计算）。这里不考虑跨
24:00的情况（也就是说，给定的数据中，结束时间总是大于等于起始时间）。
注意有的网页（如示例中的index.html）是多次访问，时间要进行相加。
输入
第一行是一个正整数，表示后面有多少条记录。
后面的是多行记录，每行记录包括：网页 开始时间 结束时间。三项数据用空格分开。
输出
访问时长最长的网页
'''

#2200015507 王一粟
n = int(input())
mydict = {}
for _ in range(n):
    name,start,end = input().split()
    h,min,s = [int(i) for i in start.split(":")]
    start = h*3600+min*60+s
    h,min,s = [int(i) for i in end.split(":")]
    end = h*3600+min*60+s
    duration = end-start
    if name in mydict:
        mydict[name] = mydict[name]+duration
    else:
        mydict[name] = duration
mylist = sorted(mydict.items(),key=lambda x:x[1],reverse=True)
print(mylist[0][0])