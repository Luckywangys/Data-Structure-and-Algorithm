'''
描述
Mr. and Mrs. Smith are going to the seaside for their holiday. Before they start off, they need to choose a hotel. They got a list of hotels from the Internet, and want to choose some candidate hotels which are cheap and close to the seashore. A candidate hotel M meets two requirements:
Any hotel which is closer to the seashore than M will be more expensive than M.
Any hotel which is cheaper than M will be farther away from the seashore than M.
输入
There are several test cases. The first line of each test case is an integer N (1 <= N <= 10000), which is the number of hotels. Each of the following N lines describes a hotel, containing two integers D and C (1 <= D, C <= 10000). D means the distance from the hotel to the seashore, and C means the cost of staying in the hotel. You can assume that there are no two hotels with the same D and C. A test case with N = 0 ends the input, and should not be processed.
输出
For each test case, you should output one line containing an integer, which is the number of all the candidate hotels.
'''

#2200015507 王一粟
while True:
    n = int(input())
    mylist = []
    if n == 0:
        break
    for i in range(n):
        d,c = [int(i) for i in input().split()]
        mylist.append([d,c])
    operate_list = sorted(mylist,key = lambda x:(x[0],x[1]))
    total = 1
    mincost = operate_list[0][1]
    nowdistance = operate_list[0][0]
    for element in operate_list[1:]:
        if element[1] < mincost:
            mincost = element[1]
            total += 1
    print(total)
