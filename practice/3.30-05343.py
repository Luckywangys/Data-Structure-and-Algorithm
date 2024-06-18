'''
描述
假设这里有36张扑克牌，分别为A1~A9,B1~B9,C1~C9,D1~D9，其中A代表方片，B代表草花，C代表红桃，D代表黑桃，那么，设定如下的排序规则：
1.对于两张卡牌，X1Y1与X2Y2，X1与X2表示A～D，Y1与Y2表示1～9，如果X1与X2不同，那么依照D>C>B>A的方式进行排序
2.假如有X1与X2相同时，那么就比较Y1与Y2的大小。
例如，对于如下的四张牌，有如下的升序排序结果：
D3，C4，A4，C1
升序排序的结果为A4，C1，C4，D3
有人提出了如下的排序策略：
先建立9个队列，用于存放点数的大小，将卡牌依点数存放入各自的队列之中，然后再按队列1到队列9依次出队。
例如，对于上面的结果，依次进队后，结果如下：
队列1：C1；队列3：D3，队列4：C4，A4
将其依次出队后，结果为C1，D3，C4，A4
然后，再建立4个队列，用于存放花色。将卡牌依花色A～D存放入队列1～4中，然后再按队列1到队列4依次出队。
例如，对于上面刚刚出队的序列C1，D3，C4，A4，将其依次进队，结果如下：
队列1：A4；队列3：C1，C4；队列4：D3
将其依次出队后，结果为A4，C1，C4，D3，排序结束。
请根据上面的算法，编写一个用队列对扑克牌排序的程序，要求依照上面的排序规则，根据先花色后点数的方法进行排序。
输入
输入分为两行，第一行为一个整数n，表示一共有n张牌（1<=n<=100）
第二行用XY的形式表示每一张牌，其中X为A～D，Y为1～9
输出
输出三个部分
第一个部分为第一次进队出队的结果，用Queue1:...表示，共9行，结果用空格分隔，下同
第二部分为第二次进队出队的结果，用QueueA:...表示，共4行
第三部分为一行，即将卡牌排序后的结果（升序排序）
'''

#2200015507 王一粟
n = int(input())
card_list = input().split()
mydict = {}
for i in range(1,10):
    mydict[i] = []
for element in card_list:
    num = int(element[-1])
    mydict[num].append(element)
queue = []
for key,value in mydict.items():
    result = " ".join(value)
    print(f"Queue{key}:{result}")
    queue.extend(value)
color_dict = {"A":[],"B":[],"C":[],"D":[]}
end = []
for element in queue:
    color_dict[element[0]].append(element)
for key,value in color_dict.items():
    end.extend(value)
    result = " ".join(value)
    print(f"Queue{key}:{result}")
print(" ".join(end))