'''
描述
深度学习模型（尤其是大模型）是近两年计算机学术和业界热门的研究方向。每个模型可以用 “模型名称-参数量” 命名，其中参数量的单位会使用两种：M，即百万；B，即十亿。同一个模型通常有多个不同参数的版本。例如，Bert-110M，Bert-340M 分别代表参数量为 1.1 亿和 3.4 亿的 Bert 模型，GPT3-350M，GPT3-1.3B 和 GPT3-175B 分别代表参数量为 3.5亿，13亿和 1750 亿的 GPT3 模型。参数量的数字部分取值在 [1, 1000) 区间（一个 8 亿参数的模型表示为 800M 而非 0.8B，10 亿参数的模型表示为 1B 而非 1000M）。计算机专业的学生小 A 从网上收集了一份模型的列表，他需要将它们按照名称归类排序，并且同一个模型的参数量从小到大排序，生成 “模型名称: 参数量1, 参数量2, ...” 的列表。请你帮他写一个程序实现。
输入
第一行为一个正整数 n（n <= 1000），表示有 n 个待整理的模型。
接下来 n 行，每行一个 “模型名称-参数量” 的字符串。模型名称是字母和数字的混合。
输出
每行一个 “模型名称: 参数量1, 参数量2, ...” 的字符串，符号均为英文符号，模型名称按字典序排列，参数量按从小到大排序。
'''

#2200015507 王一粟
n = int(input())
mydict = {}
for i in range(n):
    name,bitnum = input().split("-")
    if name not in mydict:
        if bitnum[-1] == "M":
            mydict[name] = [[(bitnum[0:-1],float(bitnum[0:-1]))],[]]
        else:
            mydict[name] = [[],[(bitnum[0:-1],float(bitnum[0:-1]))]]
    else:
        if bitnum[-1] == "M":
            mydict[name][0].append((bitnum[0:-1],float(bitnum[0:-1])))
        else:
            mydict[name][1].append((bitnum[0:-1],float(bitnum[0:-1])))
mylist = sorted(mydict.items(), key = lambda x:x[0])
for machine in mylist:
    name = machine[0]
    mbit = sorted(machine[1][0],key = lambda x:x[1])
    bbit = sorted(machine[1][1],key = lambda x:x[1])
    resultmbit = [str(i[0])+"M" for i in mbit]
    resultbbit = [str(i[0])+"B" for i in bbit]
    resultlist = resultmbit + resultbbit
    print(f"{name}:",", ".join(str(i) for i in resultlist))