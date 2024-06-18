'''
描述
Background
The knight is getting bored of seeing the same black and white squares again and again and has decided to make a journey
around the world. Whenever a knight moves, it is two squares in one direction and one square perpendicular to this. The world of a knight is the chessboard he is living on. Our knight lives on a chessboard that has a smaller area than a regular 8 * 8 board, but it is still rectangular. Can you help this adventurous knight to make travel plans?
Problem
Find a path such that the knight visits every square once. The knight can start and end on any square of the board.
输入
The input begins with a positive integer n in the first line. The following lines contain n test cases. Each test case consists of a single line with two positive integers p and q, such that 1 <= p * q <= 26. This represents a p * q chessboard, where p describes how many different square numbers 1, . . . , p exist, q describes how many different square letters exist. These are the first q letters of the Latin alphabet: A, . . .
输出
The output for every scenario begins with a line containing "Scenario #i:", where i is the number of the scenario starting at 1. Then print a single line containing the lexicographically first path that visits all squares of the chessboard with knight moves followed by an empty line. The path should be given on a single line by concatenating the names of the visited squares. Each square name consists of a capital letter followed by a number.
If no such path exist, you should output impossible on a single line.
'''

#2200015507 王一粟
def dfs(i,j,t,path):
    if t == p*q:
        result = ""
        for element in path:
            num,letter = element[0],element[1]
            result = result + chr(letter+64) + str(element[0])
        return result
    graph[i][j] = True
    for dj,di in [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]:
        if 1<=i+di<=p and 1<=j+dj<=q and graph[i+di][j+dj] is False:
            ans = dfs(i+di,j+dj,t+1,path+[(i+di,j+dj)])
            if ans != 0:
                return ans
    graph[i][j] = False
    return 0
cnt = 0
for _ in range(int(input())):
    p,q = map(int, input().split())
    if cnt != 0:
        print()
    cnt += 1
    print(f"Scenario #{cnt}:")
    graph = [[False for i in range(q+1)] for j in range(p+1)]
    d = 0
    for i in range(1,p+1):
        if d == 1:
            break
        for j in range(1,q+1):
            m = dfs(i,j,1,[(i,j)])
            if m == 0:
                continue
            else:
                d = 1
                print(m)
                break
    if d == 0:
        print("impossible")










