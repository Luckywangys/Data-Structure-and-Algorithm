'''
Q6输入
输入只有一行，由若干正整数组成，每个正整数表示这条弹幕是投票给哪个选项的。
输入的正整数个数不超过100,000，且满足最多有100个不同的选项，选项的编号不超过100,000。
输出
输出只有一行，为得票最多的选项。若有并列第一的情况出现，则按编号从小到大依次输出所有得票数最多的选项，用空格隔开。
'''

# 2200015507 王一粟
mylist = input().split()
mydict = {}
for num in mylist:
    if int(num) not in mydict:
        mydict[int(num)] = 1
    else:
        mydict[int(num)] += 1
sortdict = sorted(mydict.items(), key=lambda x: (x[1],-x[0]), reverse=True)
result = [i[0] for i in sortdict if i[1] == sortdict[0][1]]
print(" ".join(str(i) for i in result))

#思路：字典排序输出key
#耗时：20min