# 学习目标：转义字符与原字符


# 换行
print('hello\nworld')

# 制表符
print('hello\tworld')   # \t：从第1个字符开始数，每4个字符算一个\t，遇到\t时，不满的用空格补齐
print('helloooo\tworld')    # 此编译器一个制表符按8个空格算

print('hello\rworld')   # \r：重新定位到最前面输出（类似于删掉前面的内容）

print('hello\bworld')   # \b：退一个字符

print(r'hello\nworld')  # 使转义字符失效
