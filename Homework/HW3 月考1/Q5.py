'''
小明同学的家长为了让小明同学接受更好的教育，最近在考虑买某重点中学附近的房子，已知他们买房子要考虑两个因素：房子离学校的距离，以及房子的价格。现在他们有一系列备选的房子，已知这些房子距离学校的x方向距离和y方向距离，以及每栋房子的价格。小明的家长认为，只有同时满足了以下两个条件的房子H买了才是不亏的：
1.小明的家长比较精打细算，所以房子的性价比大于所用备选房子性价比的中位数（定义见下图）
2.小明的家长想攒钱，所以房子的价格小于所有备选房子价格的中位数
注：
性价比 = 房子和学校之间的交通距离 / 房子的价格
（由于该城市的街道布局接近方格状，且从学校到房子无法穿墙而过，房子H去学校的交通距离定义为，房子H距离学校的x方向距离和y方向距离的和）
现在需要你来帮小明的家长判断，一系列备选房子里，值得买的房子有多少栋。
输入
第1行为1个整数，n，代表备选房子的数目
第2行为n个房子离学校的x，y距离对，如“(x,y)”，距离均为整数
第3行为n个整数，代表每个房子的价格
输出
一个整数，代表n个房子中值得买的房子数目。
'''

# 2200015507 王一粟
n = int(input())
pairs = [i[1:-1] for i in input().split()]
distances = [sum(map(int,i.split(','))) for i in pairs]
price = [int(i) for i in input().split()]
addressprice = sorted(price)
qualpricelist = []
for inum,distance in enumerate(distances):
    qualpricelist.append(distance/price[inum])
qualpriceresult = sorted(qualpricelist)
if len(price)%2 == 0:
    price1 = addressprice[int(n/2)]
    price2 = addressprice[int(n/2) -1]
    midnum = (price1+price2)/2
    price1 = qualpriceresult[int(n / 2)]
    price2 = qualpriceresult[int(n / 2) - 1]
    midqualprice = (price1 + price2) / 2
else:
    midnum = addressprice[int((n-1)/2)]
    midqualprice = qualpriceresult[int((n - 1) / 2)]
cnt = 0
for inum,distance in enumerate(distances):
    if price[inum]<midnum and distance/price[inum] > midqualprice:
        cnt += 1
print(cnt)