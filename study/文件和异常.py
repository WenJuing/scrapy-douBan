import json


# 读取整个文件

with open('pi_digits.txt') as file_object:  # file_object只能在with块里面使用
    contents = file_object.read()
    print(contents.rstrip())

# 读取其他文件夹里的文件

with open('..\\res\\hello.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# 逐行读取

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())    # 使用rstrip()方法消除多余空白行

# 创建一个包含文件各行的列表

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# 使用文件的内容

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# 圆周率值中包含你的生日吗

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
birthday = '120372'

for line in lines:
    pi_string += line.strip()

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday not appears in the first million digits of pi!")

# 写入空文件

filename = 'message_1.txt'

with open(filename, 'a+') as file_object:   # a+:追加，且当文件不存在时自动创建文件
    file_object.write("I love programming.")    # 只能写入字符串
    file_object.write("I love programming.")

# 写入多行

filename = 'message_2.txt'

with open(filename, 'w') as file_object:   # w:写入，清空文件内容后写入，自动创建
    file_object.write("I love programming.\n")  # 通过添加换行符实现换行
    file_object.write("I love programming.\n")

# 异常

# ZeroDivisionError异常

try:
    a = 5 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# 使用异常避免崩溃

print("Give me to numbers, and I'll divide them.")
print("Enter 'q' to quit.")
'''
while True:
    first_number = input("\nGive me the first_number:")
    if first_number == 'q':
        break
    second_number = input("\nGive me the second_number:")
    if second_number == 'q':
        break
    try:
        res = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print("The result is", res)
'''

# FileNotFoundError异常

filename = 'no_such_file.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("Sorry, the " + filename + " dose not exist!")

# 分析文本

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("Sorry, the " + filename + " dose not exist!")
else:
    # 计算这本书共有多少个单词
    words = contents.split()
    count_words = len(words)
    print("The file " + filename + " has about " + str(count_words) + " words.")

# 使用多个文件


def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("Sorry, the " + filename + " dose not exist!")
    else:
        # 计算这本书共有多少个单词
        words = contents.split()
        count_words = len(words)
        print("The file " + filename + " has about " + str(count_words) + " words.")


count_words('little_women.txt')
count_words('no_such_file.txt')
count_words('moby_dick.txt')

# 失败时一声不吭


def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass    # 什么也不做
    else:
        words = contents.split()
        count_words = len(words)
        print("The file " + filename + " has about " + str(count_words) + " words.")


count_words('little_women.txt')
count_words('no_such_file.txt')
count_words('moby_dick.txt')

# json.dump()和json.load() 即存储数据也存储结构


filename = 'message.json'
num_list = [1, 2, 3, 4, 5]

with open(filename, 'w') as file_object:
    json.dump(num_list, file_object)    # 需要导入json模块

with open(filename) as file_object:
    contents = json.load(file_object)
print(contents)

# 保存和读取用户生成的数据

filename = 'username.json'

try:
    with open(filename) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("What's your name?")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    print("We'll remeber you when you back." + username)
else:
    print("Welcome back!" + username.title())

# 重构————将代码块根据功能划分为一个个函数，使代码更清晰、更易理解、更易扩展


def get_stored_username():
    '''获取用户名'''
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileExistsError:
        return None
    else:
        return username


def greet_user():
    '''问候用户，并指出名字'''
    username = get_stored_username()
    if username:
        print("Welcome back!" + username.title())
    else:
        username = input("What's your name?")
        with open(filename, 'w') as file_object:
            json.dump(username, file_object)
        print("We'll remeber you when you back." + username)


greet_user()
