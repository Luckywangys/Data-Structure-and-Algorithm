'''
描述
一年一度的保研时间又到了，XX大学XX学院即将准备推免工作。为简化问题，我们假设该学院仅按照平均绩点来进行排名，不考虑挂科，综测排名等各种因素。
推免优先级按照学生的平均绩点来决定，平均绩点更高的同学比平均绩点更低的同学更优先获得推免资格。(输入数据保证同学绩点均不相同，无需考虑绩点相同的情况）
当某门课的得分低于60分时，该门课程绩点为0，当得分score满足60<=score<=100时，分数和绩点的转换公式如下：
gpa=4-3*(100-score)**2/1600
每门课程的绩点按照 该课程的学分/总学分 的权重进行加权平均，得到平均绩点。
例如，一个同学修过三门课，三门课绩点分别是2.0,3.0,4.0 ； 三门课学分分别是2，3，3 ; 则该学生所修总学分为2+3+3=8，则三门课对应的权重分别为2/8, 3/8, 3/8
该同学平均绩点为：2.0*(2/8)+3.0*(3/8)+4.0*(3/8)=3.125
输入
第一行输入两个整数N和M，并用空格隔开，表示总共有N个同学，M个推免资格
下面是N行，每行表示一个学生的信息（保证一个同学的信息仅出现1次，不会重复出现）：
第1个数据表示该学生的学号，后面的数据两两一组，表示该学生所修某门课程的得分和该课程的学分，学分一定是整数，得分可能带有小数。数据间用空格隔开。
例如"2201111002 78 5 80 2"表示学号为2201111002的同学选修过2门课，第一门5学分得分78，第二门2学分得分80
输出
输出共一行，输出所有获得推免同学的学号，中间用空格隔开（按照平均绩点高的在前的顺序输出，输入数据保证不存在绩点相同的同学）
'''

#2200015507 王一粟
def gpa(k):
    if k < 60:
        return 0
    else:
        return 4-3*(100-k)**2/1600
def total_gpa(mylist):
    total_credit = 0
    total = 0
    cnt = 0
    for i in mylist:
        if cnt == 0:
            cnt = 1
            grade = gpa(float(i))
        else:
            cnt = 0
            credit = int(i)
            total_credit += credit
            total += credit*grade
    return total/total_credit
n,m = [int(i) for i in input().split()]
mydict = {}
for _ in range(n):
    s = input().split()
    idx = s[0]
    grade = s[1:]
    mydict[idx] = total_gpa(grade)
result_list = sorted(mydict.items(),key=lambda x:x[1],reverse = True)
result = []
for p in range(m):
    result.append(result_list[p][0])
print(" ".join(result))