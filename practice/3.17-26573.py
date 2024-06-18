'''
描述
在数学上具有重要意义的康托集(cantor set)是用如下方法构造的。考虑区间[0,1]，我们第一步要做的是，将区间三等分，然后删去中间的部分(1/3, 2/3)。在后面的每一步中，取出所有剩下的小区间，将每一个小区间都三等分后删去中间的部分，这样操作无穷次，最后剩下的点即为康托集。
在本题中，对于输入n，我们假设操作n步之后剩下的每个小区间为一个单位长度。请你用线段图表示出这些剩下的小区间。每个小区间使用一个字符‘*’表示，而[0,1]区间的其余位置按照其单位长度用相应个数的‘-’表示。
'''

#2200015507 王一粟
n = int(input())
sum_num = 3**n
mylist = [[0,sum_num]]
operate = []
for _ in range(n):
    for element in mylist:
        start,end = element[0],element[1]
        length = end-start
        small_length = length//3
        term1 = [start,start+small_length]
        term2 = [end-small_length,end]
        operate.append(term1)
        operate.append(term2)
    mylist = operate
    operate = []
result_list = [i[1] for i in mylist]
result = ["*" if i in result_list else "-" for i in range(1,sum_num+1)]
print("".join(result))