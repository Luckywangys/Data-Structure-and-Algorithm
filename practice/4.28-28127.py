'''
描述
在刚刚结束的第46届国际大学生程序设计竞赛（简称ICPC），来自全球100多个国家的200多支大学队伍同场竞技。北京大学的三位选手（王展鹏、蒋凌宇、罗煜翔）获得了全球总决赛冠军，这也是北京大学历史最好成绩。
ICPC是全世界最高水平的算法竞赛，各个国家、各个大学最优秀的选手都会参加，比赛采用组队形式，3名选手，共用1台电脑，在5小时内解决10道左右非常困难的算法问题。相比真实比赛的排名规则，本题做了一些简化，请你写个程序计算最终排名。
共有 m 个提交记录，每个提交记录包含队伍名称、提交题目的编号和是否正确（即通过评测）。排序规则为：
做对题目多的队伍排名靠前；
做对题目数相同时，总提交次数较少的队伍排名靠前；
做对题目数和总提交次数都相同时，按队伍名称的字典序排名；
按上述规则输出前 12 名的队伍信息，几点说明和提示：
如果队伍总数不足 12 名，则输出所有队伍；
如果队伍在某题 AC 后重复提交此题，这时的提交仍然记入总提交数，但重复 AC 同一题不会增加“做对题目数目”；
输入
第一行一个整数 M (1 ≤ M ≤ 1000) 表示提交记录数目。
接下去 M 行，每行一个提交记录，由逗号分隔的三部分组成，第一部分为队伍名称，仅有大小写字母和空格组成；第二部分为题目编号，必为大写字母A-Z之一；第三部分为评测结果，yes 表示通过，no 表示未通过。
输出
共 12 行（队伍总数不足 12 个时，输出全部队伍即可），按排名顺序依次输出每支队伍，包括名次（1开始）、队伍名称、做对题目数（重复AC同一题只计一次）、总提交次数，共四部分信息，信息之间用一个空格隔开。
'''

#2200015507 王一粟
m = int(input())
team_num = 0
right_num_dict = {}
team_ac_dict = {}
for _ in range(m):
    team,question,result = input().split(",")
    if team not in right_num_dict:
        team_num += 1
        right_num_dict[team] = {}
        team_ac_dict[team] = [0,0]
    team_ac_dict[team][1] += 1
    if result == "yes" and question not in right_num_dict[team]:
        right_num_dict[team][question] = 1
        team_ac_dict[team][0] += 1
result_list = sorted(team_ac_dict.items(),key = lambda x:(-x[1][0],x[1][1],x[0]))
if team_num <= 12:
    cnt = 0
    for element in result_list:
        cnt += 1
        print(cnt,element[0],element[1][0],element[1][1])
else:
    cnt = 0
    for element in result_list[:12]:
        cnt += 1
        print(cnt,element[0],element[1][0],element[1][1])










