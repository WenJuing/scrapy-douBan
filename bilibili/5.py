# 学习目标：输出函数print


# print()函数可输出数字
print(12)

# 可输出字符串
print("hello")

# 可输出表达式
print(12*3)

# 可不换行输出
print("aaa", "bbb", "ccc")

# 可将内容输入到文件
fp = open('D:/pythoncode/bilibili/5.txt', 'a+')  # 模式a+：文件不存在就创建，文件存在就追加
print("this is a content.", file=fp)
fp.close()  # open()和close()成对出现
