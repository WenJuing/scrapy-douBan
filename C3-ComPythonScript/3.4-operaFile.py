# 读写文件


def operaFile():
    '''创建文件'''
    # 参数2：a表示追加
    fp = open('test.txt', 'a')
    # 写入内容
    fp.write('Hello Python!')
    fp.close
    # 追加文件内容
    fp = open('test.txt', 'a')
    fp.write('Hello World!')
    fp.close


if __name__ == '__main__':
    operaFile()
