'''
描述
会下国际象棋的人都很清楚：皇后可以在横、竖、斜线上不限步数地吃掉其他棋子。如何将8个皇后放在棋盘上（有8 * 8个方格），使它们谁也不能被吃掉！这就是著名的八皇后问题。
对于某个满足要求的8皇后的摆放方法，定义一个皇后串a与之对应，即a=b1b2...b8，其中bi为相应摆法中第i行皇后所处的列数。已经知道8皇后问题一共有92组解（即92个不同的皇后串）。
给出一个数b，要求输出第b个串。串的比较是这样的：皇后串x置于皇后串y之前，当且仅当将x视为整数时比y小。
输入
第1行是测试数据的组数n，后面跟着n行输入。每组测试数据占1行，包括一个正整数b(1 <= b <= 92)
输出
输出有n行，每行输出对应一个输入。输出应是一个正整数，是对应于b的皇后串。
'''

#2200015507 王一粟
result = []
progress = [-1]*8
def legal(x,y):
    for i in range(x):
        origin_x,origin_y = i,progress[i]
        if origin_y == y or x-i == abs(origin_y - y):
            return False
    return True
def dfs(x,y):
    if legal(x,y):
        progress[x] = y
        if x == 7:
            result.append(int("".join(str(i+1) for i in progress)))
            progress[x] = -1
        else:
            for next_y in range(8):
                dfs(x + 1, next_y)
            progress[x] = -1
for y in range(8):
    dfs(0,y)
result.sort()
for _ in range(int(input())):
    print(result[int(input())-1])