'''
描述
In this problem, you have to analyze a particular sorting algorithm. The algorithm processes a sequence of n distinct integers by swapping two adjacent sequence elements until the sequence is sorted in ascending order. For the input sequence
9 1 0 5 4 ,
Ultra-QuickSort produces the output
0 1 4 5 9 .
Your task is to determine how many swap operations Ultra-QuickSort needs to perform in order to sort a given input sequence.
输入
The input contains several test cases. Every test case begins with a line that contains a single integer n < 500,000 -- the length of the input sequence. Each of the the following n lines contains a single integer 0 ≤ a[i] ≤ 999,999,999, the i-th input sequence element. Input is terminated by a sequence of length n = 0. This sequence must not be processed.
输出
For every input sequence, your program prints a single line containing an integer number op, the minimum number of swap operations necessary to sort the given input sequence.
'''
# 2200015507 王一粟
def merge(mylist):
    m = len(mylist)
    if m == 1:
        return mylist,0
    k = int(m//2)
    left_side,inverse_left = merge(mylist[:k])
    right_side,inverse_right = merge(mylist[k:])
    index = 0
    result = 0
    result_list = []
    for myindex,element in enumerate(left_side):
        while element > right_side[index]:
            result_list.append(right_side[index])
            result += k-myindex
            index += 1
            if index == m-k:
                break
        if index != m-k:
            result_list.append(element)
        else:
            result_list.extend(left_side[myindex:])
            break
    if index != m-k:
        result_list.extend(right_side[index:])
    return result_list,inverse_left+inverse_right+result

while True:
    n = int(input())
    if n == 0:
        break
    mylist = []
    for _ in range(n):
        mylist.append(int(input()))
    result_list,inverse_num = merge(mylist)
    print(inverse_num)