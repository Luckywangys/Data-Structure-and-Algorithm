'''
描述
据我国史料记载，现在植被稀少的黄土高原、渭河流域也曾是森林遍布、山清水秀。楼兰古城因屯垦开荒、盲目灌溉，导致孔雀河改道而衰落。自然生态的变迁决定着人类文明的兴衰更替。习近平总书记在阐述生态与文明的关系时指出：“生态兴则文明兴，生态衰则文明衰”。
2013年4月2日，习近平总书记在参加首都义务植树活动时指出，我们必须清醒地看到，我国总体上仍然是一个缺林少绿、生态脆弱的国家，植树造林，改善生态，任重而道远。
2020年，习近平总书记在参加首都义务植树活动时强调，要牢固树立“绿水青山就是金山银山”的理念，加强生态保护和修复，扩大城乡绿色空间，为人民群众植树造林，努力打造青山常在、绿水长流、空气常新的美丽中国。
为了更科学地植树造林，需要对现有树木的种类进行统计，你能完成这个任务，为建设生态文明贡献一己之力吗？
输入
输入第一行给出一个正整数N（N<=100000),为树的数量。随后的N行，每行给出卫星观测到的一颗树的种类名称。种类名称是不超过30个英文字母和空格组成的字符串。
输出
按字典序递增输出各种树的种类名称及其所占总数的百分比，其间以空格分隔，精确到小数点后四位
'''

#2200015507 王一粟
mydict = {}
n = int(input())
for _ in range(n):
    s = input()
    if s in mydict:
        mydict[s] += 1
    else:
        mydict[s] = 1
mylist = sorted(mydict.items())
for element in mylist:
    num = element[1]/n*100
    print(element[0],f"{num:.4f}%")