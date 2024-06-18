'''
描述
Farmer John has been elected mayor of his town! One of his campaign promises was to bring internet connectivity to all farms in the area. He needs your help, of course.
Farmer John ordered a high speed connection for his farm and is going to share his connectivity with the other farmers. To minimize cost, he wants to lay the minimum amount of optical fiber to connect his farm to all the other farms.
Given a list of how much fiber it takes to connect each pair of farms, you must find the minimum amount of fiber needed to connect them all together. Each farm must connect to some other farm such that a packet can flow from any one farm to any other farm.
The distance between any two farms will not exceed 100,000.
输入
The input includes several cases. For each case, the first line contains the number of farms, N (3 <= N <= 100). The following lines contain the N x N conectivity matrix, where each element shows the distance from on farm to another. Logically, they are N lines of N space-separated integers. Physically, they are limited in length to 80 characters, so some lines continue onto others. Of course, the diagonal will be 0, since the distance from farm i to itself is not interesting for this problem.
输出
For each case, output a single integer length that is the sum of the minimum length of fiber required to connect the entire set of farms.
'''

#2200015507 王一粟
import heapq

while True:
    try:
        n = int(input())
        graph = []
        wait_list = []
        total = 0
        while True:
            a = [int(i) for i in input().split()]
            wait_list = wait_list + a
            total += len(a)
            if total == n ** 2:
                break
        cnt = 0
        for i in range(n):
            mylist = []
            for j in range(n):
                mylist.append(wait_list[cnt])
                cnt += 1
            graph.append(mylist)
        visited = [False for i in range(n)]
        mylist = []
        heapq.heappush(mylist, [0, 0])
        result = 0
        cnt = 0
        while cnt < n:
            distance, node = heapq.heappop(mylist)
            if visited[node] is True:
                continue
            visited[node] = True
            cnt += 1
            result += distance
            for idx, element in enumerate(graph[node]):
                if visited[idx] is False:
                    heapq.heappush(mylist, [element, idx])
        print(result)
    except:
        break