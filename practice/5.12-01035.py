'''
描述
现在有一些英语单词需要做拼写检查，你的工具是一本词典。需要检查的单词，有的是词典中的单词，有的与词典中的单词相似，你的任务是发现这两种情况。单词A与单词B相似的情况有三种：
1、删除单词A的一个字母后得到单词B；
2、用任意一个字母替换单词A的一个字母后得到单词B；
3、在单词A的任意位置增加一个字母后得到单词B。
你的任务是发现词典中与给定单词相同或相似的单词。
输入
第一部分是词典中的单词，从第一行开始每行一个单词，以"#"结束。词典中的单词保证不重复，最多有10000个。
第二部分是需要查询的单词，每行一个，以"#"结束。最多有50个需要查询的单词。
词典中的单词和需要查询的单词均由小写字母组成，最多包含15个字符。
输出
按照输入的顺序，为每个需要检查的单词输出一行。如果需要检查的单词出现在词典中，输出“?x is correct"，?x代表需要检查的单词。如果需要检查的单词没有出现在词典中，则输出"?x: ?x1 ?x2 ...?xn"，其中?x代表需要检查的单词，?x1...?xn代表词典中与需要检查的单词相似的单词，这些单词中间以空格隔开。如果没有相似的单词，输出"?x:"即可。
'''

#2200015507 王一粟
mylist = []
while True:
    s = input()
    if s == "#":
        break
    else:
        mylist.append(s)
while True:
    word = input()
    cnt = 0
    if word == "#":
        break
    for element in mylist:
        if word == element:
            print(f"{word} is correct")
            cnt = 1
            break
    if cnt == 1:
        continue
    result_list = []
    length = len(word)
    for element in mylist:
        if length == len(element):
            modified = 0
            for i in range(length):
                if element[i] != word[i]:
                    modified += 1
                    if modified >= 2:
                        break
            if modified == 1:
                result_list.append(element)
        elif length == len(element) - 1:
            i,j = 0,0
            modified = 0
            while i<len(element) and j<len(word):
                if element[i] != word[j]:
                    modified += 1
                    i += 1
                    if modified >= 2:
                        break
                else:
                    i += 1
                    j += 1
            if modified == 1 or modified == 0:
                result_list.append(element)
        elif length == len(element) + 1:
            i,j = 0,0
            modified = 0
            while i<len(element) and j<len(word):
                if element[i] != word[j]:
                    modified += 1
                    j += 1
                    if modified >= 2:
                        break
                else:
                    i += 1
                    j += 1
            if modified == 1 or modified == 0:
                result_list.append(element)
    if result_list:
        print(f"{word}: "+" ".join(result_list))
    else:
        print(f"{word}:")