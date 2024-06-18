'''
描述
An ascending sorted sequence of distinct values is one in which some form of a less-than operator is used to order the elements from smallest to largest. For example, the sorted sequence A, B, C, D implies that A < B, B < C and C < D. in this problem, we will give you a set of relations of the form A < B and ask you to determine whether a sorted order has been specified or not.
输入
Input consists of multiple problem instances. Each instance starts with a line containing two positive integers n and m. the first value indicated the number of objects to sort, where 2 <= n <= 26. The objects to be sorted will be the first n characters of the uppercase alphabet. The second value m indicates the number of relations of the form A < B which will be given in this problem instance. Next will be m lines, each containing one such relation consisting of three characters: an uppercase letter, the character "<" and a second uppercase letter. No letter will be outside the range of the first n letters of the alphabet. Values of n = m = 0 indicate end of input.
输出
For each problem instance, output consists of one line. This line should be one of the following three:
Sorted sequence determined after xxx relations: yyy...y.
Sorted sequence cannot be determined.
Inconsistency found after xxx relations.
where xxx is the number of relations processed at the time either a sorted sequence is determined or an inconsistency is found, whichever comes first, and yyy...y is the sorted, ascending sequence.
'''

#2200015507 王一粟
from collections import deque
def bfs(n,zero_degree):
    queue = deque([i for i in initial.keys()])
    q = zero_degree
    result = []
    spot = 0
    while queue:
        if len(queue) > 1:
            spot = 1
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            t[neighbor] -= 1
            if t[neighbor] == 0:
                q += 1
                queue.append(neighbor)
    if q != n:
        return 0
    if spot == 1:
        return 1
    out = [chr(i+65) for i in result]
    return "".join(out)
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    initial = {i:1 for i in range(n)}
    graph = [[] for i in range(n)]
    degree = [0 for j in range(n)]
    zero_degree = n
    mylist = []
    for _ in range(m):
        a,b,c = list(input())
        mylist.append((a,b,c))
    p = 0
    cnt = 0
    for element in mylist:
        cnt += 1
        small,op,big = ord(element[0])-65,element[1],ord(element[2])-65
        graph[small].append(big)
        if degree[big] == 0:
            zero_degree -= 1
            del initial[big]
        degree[big] += 1
        t = degree.copy()
        m = bfs(n,zero_degree)
        if m == 0:
            p = 1
            print(f"Inconsistency found after {cnt} relations.")
            break
        if m == 1:
            continue
        p = 1
        print(f"Sorted sequence determined after {cnt} relations: {m}.")
        break
    if p == 0:
        print("Sorted sequence cannot be determined.")


