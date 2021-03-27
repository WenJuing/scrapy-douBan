# 字符串函数的使用

S = "This is a APPLE"
print("例句：%s" % S)


def strCase():
    "字符串大小转换"
    print("S.upper()全部大写:%s" % (S.upper()))
    print("S.lower()全部小写:%s" % (S.lower()))


def strFind():
    "字符串搜索、替换"
    print("S.find('is')寻找第一个is出现的位置：%s" % S.find('is'))
    print("S.count('is')计算is出现的次数：%s" % S.count('is'))
    print("S.replace('is','##')把is替换为##：%s" % S.replace('is', '##'))


def strSplit():
    "字符串分割、组合"
    print("S.split()字符串分割：%s" % S.split())
    print("#.join(['apple','banana','cucumber'])字符串连接（用#连接）：%s" % '#'.join(['apple', 'banana', 'cucumber']))


if __name__ == '__main__':
    strCase()
    strFind()
    strSplit()
