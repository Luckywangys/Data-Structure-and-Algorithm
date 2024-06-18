'''
描述
因疫情防控需要，每名同学需要遵守“三天一检”的核酸要求，即每三天至少需要做一次核酸检测。现在需要统计学校同学近9天内的核酸检测完成情况，其中每名同学第一天必须完成一次核酸检测。请输出有多少名同学没有按时完成核酸检测，并输出完成情况（未按时完成核酸的学生数量除以院系总人数）最差的院系编号。
输入
第一行是整数n，为学生数量；
第二行是整数m，为核酸检测信息数量；
接下来先有n行，每行为学生的基本信息，即学生编号和院系编号，用空格隔开；
最后为m行核酸检测信息，每行为检测日期和学生编号，用空格隔开。其中，检测日期为1～9的数字。
输出
第一行为没有按时完成核酸检测的学生数量；
第二行为完成情况最差的院系编号
'''

#2200015507 王一粟
def judge(mylist):
    m = sorted(mylist)
    length = len(m)
    if m[0] != 1:
        return False
    for i in range(1,length):
        if m[i]-m[i-1]>=4:
            return False
    if 9-m[-1]>=3:
        return False
    return True
n = int(input())
m = int(input())
school_dict = {}
stu_dict = {}
mydict = {}
for _ in range(n):
    stu,school = [i for i in input().split()]
    school_dict[stu] = school
    stu_dict[stu] = []
    if school not in mydict:
        mydict[school] = 1
    else:
        mydict[school] = mydict[school]+1

for _ in range(m):
    day,idx = input().split()
    day = int(day)
    stu_dict[idx].append(day)
cnt = 0
cnt_school = {}
for idx,day_list in stu_dict.items():
    if not judge(day_list):
        cnt += 1
        school = school_dict[idx]
        if school not in cnt_school:
            cnt_school[school] = 1
        else:
            cnt_school[school] = cnt_school[school] + 1
school_idx = sorted(cnt_school.items(),key = lambda x:x[1]/mydict[x[0]],reverse = True)
print(cnt)
print(school_idx[0][0])