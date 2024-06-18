'''
描述
《Journey to the West》(also 《Monkey》) is one of the Four Great Classical Novels of Chinese literature. It was written by Wu Cheng'en during the Ming Dynasty. In this novel, Monkey King Sun Wukong, pig Zhu Bajie and Sha Wujing, escorted Tang Monk to India to get sacred Buddhism texts.
During the journey, Tang Monk was often captured by demons. Most of demons wanted to eat Tang Monk to achieve immortality, but some female demons just wanted to marry him because he was handsome. So, fighting demons and saving Monk Tang is the major job for Sun Wukong to do.
Once, Tang Monk was captured by the demon White Bones. White Bones lived in a palace and she cuffed Tang Monk in a room. Sun Wukong managed to get into the palace. But to rescue Tang Monk, Sun Wukong might need to get some keys and kill some snakes in his way.
The palace can be described as a matrix of characters. Each character stands for a room. In the matrix, 'K' represents the original position of Sun Wukong, 'T' represents the location of Tang Monk and 'S' stands for a room with a snake in it. Please note that there are only one 'K' and one 'T', and at most five snakes in the palace. And, '.' means a clear room as well '#' means a deadly room which Sun Wukong couldn't get in.
There may be some keys of different kinds scattered in the rooms, but there is at most one key in one room. There are at most 9 kinds of keys. A room with a key in it is represented by a digit(from '1' to '9'). For example, '1' means a room with a first kind key, '2' means a room with a second kind key, '3' means a room with a third kind key... etc. To save Tang Monk, Sun Wukong must get ALL kinds of keys(in other words, at least one key for each kind).
For each step, Sun Wukong could move to the adjacent rooms(except deadly rooms) in 4 directions(north,west,south and east), and each step took him one minute. If he entered a room in which a living snake stayed, he must kill the snake. Killing a snake also took one minute. If Sun Wukong entered a room where there is a key of kind N, Sun would get that key if and only if he had already got keys of kind 1,kind 2 ... and kind N-1. In other words, Sun Wukong must get a key of kind N before he could get a key of kind N+1 (N>=1). If Sun Wukong got all keys he needed and entered the room in which Tang Monk was cuffed, the rescue mission is completed. If Sun Wukong didn't get enough keys, he still could pass through Tang Monk's room. Since Sun Wukong was a impatient monkey, he wanted to save Tang Monk as quickly as possible. Please figure out the minimum time Sun Wukong needed to rescue Tang Monk.
输入
There are several test cases.
For each case, the first line includes two integers N and M(0 < N <= 100, 0 <= M <= 9), meaning that the palace is a N * N matrix and Sun Wukong needed M kinds of keys(kind 1, kind 2, ... kind M).
Then the N*N matrix follows.
The input ends with N = 0 and M = 0.
输出
For each test case, print the minimum time (in minute) Sun Wokong needed to save Tang Monk. If it's impossible for Sun Wokong to complete the mission, print "impossible".
'''

#2200015507 王一粟
from collections import deque
while True:
    n,m = [int(i) for i in input().split()]
    if n == 0 and m == 0:
        break
    graph = []
    for i in range(n):
        s = list(input())
        if "K" in s:
            start_x,start_y = i,s.index("K")
        if "T" in s:
            end_x,end_y = i,s.index("T")
        graph.append(s)
    visited = [[False for j in range(n)] for i in range(n)]
    queue = deque([[start_x,start_y,0,0,set()]])
    cnt = 0
    visited[start_x][start_y] = 0
    wait_queue = deque()
    now_time = 0
    while wait_queue or queue:
        if not queue:
            queue = wait_queue
            now_time = wait_queue[0][3]
            wait_queue = deque()
        if cnt == 1: break
        x,y,key_nums,time,path = queue.popleft()
        if x == end_x and y == end_y and key_nums == m:
            print(time)
            cnt = 1
            break
        if now_time != time:
            now_time = time
            queue = queue + wait_queue
            wait_queue = deque()
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            if 0<=dx+x<n and 0<=dy+y<n and graph[x+dx][y+dy] != "#":
                if graph[x+dx][y+dy] == ".":
                    if visited[x+dx][y+dy] is False:
                        visited[x+dx][y+dy] = key_nums
                        queue.append([x+dx,y+dy,key_nums,time+1,path])
                    else:
                        if visited[x+dx][y+dy] < key_nums:
                            visited[x+dx][y+dy] = key_nums
                            queue.append([x+dx,y+dy,key_nums,time+1,path])
                elif graph[x+dx][y+dy] == "S":
                    if visited[x+dx][y+dy] is False:
                        visited[x+dx][y+dy] = key_nums
                        wait_queue.append([x+dx,y+dy,key_nums,time+2,path | {(x+dx,y+dy)}])
                    else:
                        if visited[x+dx][y+dy] < key_nums:
                            visited[x+dx][y+dy] = key_nums
                            if (x+dx,y+dy) not in path:
                                wait_queue.append([x+dx, y+dy, key_nums, time+2, path|{(x+dx, y+dy)}])
                            else:
                                queue.append([x+dx,y+dy,key_nums,time+1,path])
                elif graph[x+dx][y+dy] == "K":
                    if visited[x+dx][y+dy]<key_nums:
                        visited[x+dx][y+dy] = key_nums
                        queue.append([x+dx, y+dy, key_nums, time+1,path])
                elif graph[x+dx][y+dy] == "T":
                    if visited[x+dx][y+dy] is False:
                        visited[x+dx][y+dy] = key_nums
                        queue.append([x+dx,y+dy,key_nums,time+1,path])
                    else:
                        if visited[x+dx][y+dy] < key_nums:
                            visited[x+dx][y+dy] = key_nums
                            queue.append([x+dx,y+dy,key_nums,time+1,path])
                else:
                    the_key = int(graph[x+dx][y+dy])
                    if the_key == key_nums + 1:
                        visited[x+dx][y+dy] = the_key
                        queue.append([x+dx,y+dy,the_key,time+1,path])
                    elif visited[x+dx][y+dy] is False:
                        visited[x+dx][y+dy] = key_nums
                        queue.append([x+dx,y+dy,key_nums,time+1,path])
                    else:
                        if visited[x+dx][y+dy] < key_nums:
                            visited[x+dx][y+dy] = key_nums
                            queue.append([x+dx,y+dy,key_nums,time+1,path])
    if cnt == 0:
        print("impossible")