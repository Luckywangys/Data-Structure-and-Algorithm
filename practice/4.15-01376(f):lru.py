'''
描述
The Robot Moving Institute is using a robot in their local store to transport different items. Of course the robot should spend only the minimum time necessary when travelling from one place in the store to another. The robot can move only along a straight line (track). All tracks form a rectangular grid. Neighbouring tracks are one meter apart. The store is a rectangle N x M meters and it is entirely covered by this grid. The distance of the track closest to the side of the store is exactly one meter. The robot has a circular shape with diameter equal to 1.6 meter. The track goes through the center of the robot. The robot always faces north, south, west or east. The tracks are in the south-north and in the west-east directions. The robot can move only in the direction it faces. The direction in which it faces can be changed at each track crossing. Initially the robot stands at a track crossing. The obstacles in the store are formed from pieces occupying 1m x 1m on the ground. Each obstacle is within a 1 x 1 square formed by the tracks. The movement of the robot is controlled by two commands. These commands are GO and TURN.
The GO command has one integer parameter n in {1,2,3}. After receiving this command the robot moves n meters in the direction it faces.
The TURN command has one parameter which is either left or right. After receiving this command the robot changes its orientation by 90o in the direction indicated by the parameter.
The execution of each command lasts one second.
Help researchers of RMI to write a program which will determine the minimal time in which the robot can move from a given starting point to a given destination.
输入
The input consists of blocks of lines. The first line of each block contains two integers M <= 50 and N <= 50 separated by one space. In each of the next M lines there are N numbers one or zero separated by one space. One represents obstacles and zero represents empty squares. (The tracks are between the squares.) The block is terminated by a line containing four positive integers B1 B2 E1 E2 each followed by one space and the word indicating the orientation of the robot at the starting point. B1, B2 are the coordinates of the square in the north-west corner of which the robot is placed (starting point). E1, E2 are the coordinates of square to the north-west corner of which the robot should move (destination point). The orientation of the robot when it has reached the destination point is not prescribed. We use (row, column)-type coordinates, i.e. the coordinates of the upper left (the most north-west) square in the store are 0,0 and the lower right (the most south-east) square are M - 1, N - 1. The orientation is given by the words north or west or south or east. The last block contains only one line with N = 0 and M = 0.
输出
The output contains one line for each block except the last block in the input. The lines are in the order corresponding to the blocks in the input. The line contains minimal number of seconds in which the robot can reach the destination point from the starting point. If there does not exist any path from the starting point to the destination point the line will contain -1.
'''
#注：出现多个输入时候慎用lru（在函数中使用每次循环不同的列表时，lru很有可能吧上个测试中的函数拿去用）
#2200015507 王一粟
from collections import deque
from functools import lru_cache
def valid_position(x,y):
    if x<0 or y<0 or x>m-1 or y>n-1:
        return True
    if graph[x][y] == 0:
        return True
    else:
        return False
def possible_direction(direction):
    if direction == "north" or direction == "south":
        return ["east","west"]
    if direction == "east" or direction == "west":
        return ["south","north"]
def direction_path_valid(direction):
    if direction == "north":
        return [[-1,0],[-2,0],[-3,0]]
    elif direction == "south":
        return [[1,0],[2,0],[3,0]]
    elif direction == "west":
        return [[0,-1],[0,-2],[0,-3]]
    elif direction == "east":
        return [[0,1],[0,2],[0,3]]
while True:
    m, n = [int(i) for i in input().split()]
    if m == 0 and n == 0:
        break
    graph = []
    for _ in range(m):
        graph.append([int(i) for i in input().split()])
    visited = [[{"north": False, "south": False, "west": False, "east": False} for j in range(n+1)] for i in range(m+1)]
    start_x, start_y, end_x, end_y, direction = input().split()
    start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(end_x), int(end_y)
    visited[start_x][start_y][direction] = True
    queue = deque([[start_x,start_y,direction,0]])
    cnt = 0
    while queue:
        x,y,direction,time = queue.popleft()
        if x == end_x and y == end_y:
            cnt = 1
            print(time)
            break
        for new_dir in possible_direction(direction):
            if visited[x][y][new_dir] is False:
                visited[x][y][new_dir] = True
                queue.append([x,y,new_dir,time+1])
        for dx,dy in direction_path_valid(direction):
            if valid_position(x + dx - 1, y + dy - 1) and valid_position(x + dx, y + dy - 1) and valid_position(x + dx - 1, y + dy) and valid_position(x + dx, y + dy):
                if 0 < x + dx < m and 0 < y + dy < n and visited[x + dx][y + dy][direction] is False:
                    visited[x + dx][y + dy][direction] = True
                    queue.append([x + dx, y + dy, direction, time + 1])
            else:
                break
    if cnt == 0:
        print(-1)