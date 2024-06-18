"""
描述
形如a3= b3 + c3 + d3的等式被称为完美立方等式。例如123= 63 + 83 + 103 。编写一个程序，对任给的正整数N (N≤100)，寻找所有的四元组(a, b, c, d)，使得a3 = b3 + c3 + d3，其中a,b,c,d 大于 1, 小于等于N，且b<=c<=d。
输入
一个正整数N (N≤100)。
输出
每行输出一个完美立方。输出格式为：
Cube = a, Triple = (b,c,d)
其中a,b,c,d所在位置分别用实际求出四元组值代入。
请按照a的值，从小到大依次输出。当两个完美立方等式中a的值相同，则b值小的优先输出、仍相同则c值小的优先输出、再相同则d值小的先输出。
"""

#2200015507 王一粟
def cube(n):
    for a in range(2,n+1):
        for b in range(2,a+1):
            for c in range(b,a+1):
                    for d in range(c,a+1):
                        if a**3 == b**3 + c**3 + d**3:
                            print(f"Cube = {a}, Triple = ({b},{c},{d})")
n = int(input())
cube(n)


