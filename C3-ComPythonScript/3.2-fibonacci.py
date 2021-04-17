# 输出斐波那契数列
def bibon(n):
    n1 = 0
    n2 = 1
    print("%d %d " % (n1, n2), end='')
    for i in range(0, n+1):
        n3 = n2 + n1
        print(n3, end=' ')
        n1 = n2
        n2 = n3


listLenStr = input("请输入fibonacci数列的长度（3~50）：")
try:
    listLen = int(listLenStr)
except ValueError:
    print("输入值类型不正确！")
    exit()
if listLen < 3 or listLen > 50:
    print("值超过范围！")
    exit()
bibon(listLen)
