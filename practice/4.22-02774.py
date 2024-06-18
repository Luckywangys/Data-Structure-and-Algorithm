'''
描述
木材厂有一些原木，现在想把这些木头切割成一些长度相同的小段木头，需要得到的小段的数目是给定了。当然，我们希望得到的小段越长越好，你的任务是计算能够得到的小段木头的最大长度。
木头长度的单位是厘米。原木的长度都是正整数，我们要求切割得到的小段木头的长度也要求是正整数。
输入
第一行是两个正整数N和K(1 ≤ N ≤ 10000, 1 ≤ K ≤ 10000)，N是原木的数目，K是需要得到的小段的数目。
接下来的N行，每行有一个1到10000之间的正整数，表示一根原木的长度。
输出
输出能够切割得到的小段的最大长度。如果连1厘米长的小段都切不出来，输出"0"。
'''

#2200015507 王一粟
n,k = [int(i) for i in input().split()]
least_num = k//n + 1
wood_list = []
for i in range(n):
    wood_list.append(int(input()))
wood_list.sort()
length = wood_list[-1]//least_num
cnt = 0
while length >= 1:
    result = 0
    for element in wood_list:
        result += element//length
    if result >= k:
        print(length)
        cnt = 1
        break
    length -= 1
if cnt == 0:
    print(0)

