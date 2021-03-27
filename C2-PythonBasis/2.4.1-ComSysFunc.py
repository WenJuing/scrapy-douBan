# 常用内置函数
n = -5
li = [1, 2, 3]
tu = ("a", "b", "c")

print("n的值：%d" % n)
print("list的值：%s" % li)
print("tuple的值：%s" % list(tu))
# abs()取绝对值
print("n的绝对值为：%d" % abs(n))
# max()取最大值
print("list的最大值：%d" % max(li))
# min()取最小值
print("list的最小值：%d" % min(li))
# divmod()取模
print("7除3=%s" % list(divmod(7, 3)))
# len()计算长度
print("list和tuple的长度分别为：%d %d" % (len(li), len(tu)))
print("\n")

# 高级内置函数
print("高级内置函数")
# lambda函数
# f = lambda x: x * 2 + 1 不推荐
def f(x): return x * x


print(f(5))


# map函数和fileter函数
def g(x):
    return x * x


def printSeq(seq):
    for i in seq:
        print(i)


def g2(x):
    if x % 2 == 0:
        return x * x
    else:
        pass


li2 = (x for x in range(1, 11))  # 用for生成元组（此时li2为生成器）
li3 = [x for x in range(1, 11)]
printSeq(map(g, li))
printSeq(map(g, li2))
print(li2)  # print无法打印生成器
printSeq(li2)   # for无法遍历生成器
print("li2生成器")
printSeq(filter(g2, li2))
print("li3列表")
printSeq(filter(g2, li3))   # filter调用条件函数，不符合条件的不输出
print("map(g2, li3):")
printSeq(map(g2, li3))   # map调用条件函数，不符合条件的输出None
