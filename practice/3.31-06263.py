'''
描述
输入一个布尔表达式，请你输出它的真假值。
比如：( V | V ) & F & ( F | V )
V表示true，F表示false，&表示与，|表示或，!表示非。
上式的结果是F
输入
输入包含多行，每行一个布尔表达式，表达式中可以有空格，总长度不超过1000
输出
对每行输入，如果表达式为真，输出"V",否则出来"F"
'''
#2200015507 王一粟
while True:
    try:
        s = input()
        s1 = s.replace("V", " True ").replace("F", " False ").replace("!"," not ").replace("|"," or ").replace("&"," and ")
        result = eval(s1)
        if result:
            print("V")
        else:
            print("F")
    except:
        break