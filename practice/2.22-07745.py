"""
描述
给定10个整数的序列，要求对其重新排序。排序要求:
1.奇数在前，偶数在后；
2.奇数按从大到小排序；
3.偶数按从小到大排序。
输入
输入一行，包含10个整数，彼此以一个空格分开，每个整数的范围是大于等于0，小于等于100。
输出
按照要求排序后输出一行，包含排序后的10个整数，数与数之间以一个空格分开。
"""

#2200015507 王一粟
mylist = input().split()
oddlist = [int(i) for i in mylist if int(i)%2 == 1]
evenlist = [int(i) for i in mylist if int(i)%2 == 0]
oddresult = sorted(oddlist,reverse=True)
evenresult = sorted(evenlist)
result = oddresult + evenresult
print(" ".join(str(k)for k in result))







