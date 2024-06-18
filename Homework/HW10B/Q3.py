'''
描述
You are given two pots, having the volume of A and B liters respectively. The following operations can be performed:
FILL(i)        fill the pot i (1 ≤ i ≤ 2) from the tap;

DROP(i)      empty the pot i to the drain;

POUR(i,j)    pour from pot i to pot j; after this operation either the pot j is full (and there may be some water left in the pot i), or the pot i is empty (and all its contents have been moved to the pot j).
Write a program to find the shortest possible sequence of these operations that will yield exactly C liters of water in one of the pots.
输入
On the first and only line are the numbers A, B, and C. These are all integers in the range from 1 to 100 and C≤max(A,B).
输出
The first line of the output must contain the length of the sequence of operations K. The following K lines must each describe one operation. If there are several sequences of minimal length, output any one of them. If the desired result can’t be achieved, the first and only line of the file must contain the word ‘impossible’.
'''

#2200015507 王一粟
from collections import deque
a,b,c = [int(i) for i in input().split()]
queue = deque([[0,0,[]]])
visited = [[0,0]]
cnt = 0
while queue:
    current_a,current_b,current_step = queue.popleft()
    if current_a == c or current_b == c:
        print(len(current_step))
        cnt = 1
        for element in current_step:
            print(element)
        break
    if current_a < a and [a,current_b] not in visited:
        queue.append([a,current_b,current_step+["FILL(1)"]])
        visited.append([a,current_b])
    if current_b < b and [current_a,b] not in visited:
        queue.append([current_a,b,current_step+["FILL(2)"]])
        visited.append([current_a,b])
    if current_a < a and current_b > 0:
        next_a = min(a,current_a+current_b)
        next_b = current_a+current_b - next_a
        if [next_a,next_b] not in visited:
            queue.append([next_a,next_b,current_step+["POUR(2,1)"]])
            visited.append([next_a,next_b])
    if current_b < b and current_a > 0:
        next_b = min(b,current_a+current_b)
        next_a = current_a + current_b - next_b
        if [next_a, next_b] not in visited:
            queue.append([next_a,next_b,current_step+["POUR(1,2)"]])
            visited.append([next_a, next_b])
    if current_b > 0 and [current_a,0] not in visited:
        queue.append([current_a,0,current_step+["DROP(2)"]])
        visited.append([current_a,0])
    if current_a > 0:
        queue.append([0,current_b,current_step+["DROP(1)"]])
        visited.append([0,current_b])
if cnt == 0:
    print("impossible")