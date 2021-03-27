# 在vscode中如何调试程序
# 1、在第10行打上断点（什么？你不会打断点？鼠标悬停在第10行最右侧，看到红色的点了吗，点它！）
# 2、按下F5，接下来就可以通过F11进行单步调试了（注意观察右边的变动情况）
def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n-1)


def main():
    '''这是一个求阶乘的程序'''
    n = input("输入一个正整数：")
    try:
        n = int(n)
    except ValueError:
        print("输入的格式不正确！")
    print("%d!=%d" % (n, fac(n)))


if __name__ == '__main__':
    m = main()
