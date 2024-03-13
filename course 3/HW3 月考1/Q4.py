'''
描述
某学院的学生都需要在某月的1号到2号期间完成课程实验，他们每个人的实验需要持续不同的时长。而实验室管理员要安排这些学生，按照一定顺序，在1号到2号期间全部完成实验。假设该学院的实验室同时只能容纳一名学生实验，而这些学生都非常积极，都希望被排在1号的第一个尽快完成实验。
假设该学院有n个学生，实验室管理员收到了n个学生每位需要占用实验室的时长T1,T2,...,Tn，由于学生发送预约邮件的时间比较接近，没办法完全按照先到先得的办法给学生分配实验时间（实验时间相同的话，先到先得）。管理员很犯愁，他希望有一种能让所有学生平均等待时间尽可能小的顺序，来安排这n位同学的实验时间，请问你能帮帮他吗？
输入
输入为2行
第一行为n，为学生人数(n<=1000)
第二行分别表示第一位学生到第n位学生的实验时长T1，T2，…，Tn，每个数据间有一个空格
输出
输出为2行
第一行为一种学生实验顺序，即1到n的一种排列
第二行为这种方案下的平均等待时间（精确到小数点后两位）
'''

#2200015507 王一粟
n = int(input())
mylist = [float(i) for i in input().split()]
mydict = {}
for i,element in enumerate(mylist):
    mydict[i+1] = element
sortlist = sorted(mydict.items(),key = lambda x:(x[1],x[0]))
resultlist = []
waittime = 0
totaltime = 0
for element in sortlist:
    resultlist.append(element[0])
    totaltime = waittime+totaltime
    waittime = waittime + element[1]
print(" ".join(str(i) for i in resultlist))
result = totaltime/n
print(f"{result:.2f}")