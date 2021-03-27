def isEvenNum(num):
    if num % 2 == 0:
        print("%d是偶数" % num)
    else:
        print("%d是奇数" % num)


if __name__ == '__main__':
    numStr = input("请输入一个整数：")
    try:
        num = int(numStr)
    except ValueError as e:
        print("错误：%s" % e)
        exit()

    isEvenNum(num)
