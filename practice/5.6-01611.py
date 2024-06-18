'''
描述
Severe acute respiratory syndrome (SARS), an atypical pneumonia of unknown aetiology, was recognized as a global threat in mid-March 2003. To minimize transmission to others, the best strategy is to separate the suspects from others.
In the Not-Spreading-Your-Sickness University (NSYSU), there are many student groups. Students in the same group intercommunicate with each other frequently, and a student may join several groups. To prevent the possible transmissions of SARS, the NSYSU collects the member lists of all student groups, and makes the following rule in their standard operation procedure (SOP).
Once a member in a group is a suspect, all members in the group are suspects.
However, they find that it is not easy to identify all the suspects when a student is recognized as a suspect. Your job is to write a program which finds all the suspects.
输入
The input file contains several cases. Each test case begins with two integers n and m in a line, where n is the number of students, and m is the number of groups. You may assume that 0 < n <= 30000 and 0 <= m <= 500. Every student is numbered by a unique integer between 0 and n−1, and initially student 0 is recognized as a suspect in all the cases. This line is followed by m member lists of the groups, one line per group. Each line begins with an integer k by itself representing the number of members in the group. Following the number of members, there are k integers representing the students in this group. All the integers in a line are separated by at least one space.
A case with n = 0 and m = 0 indicates the end of the input, and need not be processed.
输出
For each case, output the number of suspects in one line.
'''

#2200015507 王一粟
def find(x):
    if parent[x] == x:
        return parent[x]
    else:
        parent[x] = find(parent[x])
        return parent[x]
def disjoint(x,y):
    rep_x,rep_y = find(x),find(y)
    if rep_x != rep_y:
        if rank[rep_x] < rank[rep_y]:
            parent[rep_x] = rep_y
        elif rank[rep_x] > rank[rep_y]:
            parent[rep_y] = rep_x
        else:
            parent[rep_y] = rep_x
            rank[rep_x] += 1
def joint(mylist):
    node = mylist[0]
    for element in mylist[1:]:
        disjoint(node,element)
while True:
    n,m = [int(i) for i in input().split()]
    if n == 0 and m == 0:
        break
    parent = [i for i in range(n)]
    rank = [0 for i in range(n)]
    for i in range(m):
        s = [int(i) for i in input().split()]
        joint(s[1:])
    rep_0 = find(0)
    print(len([i for i in parent if find(i) == rep_0]))