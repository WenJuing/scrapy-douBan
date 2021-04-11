# 双引号

str1 = '人生苦短，我用Python'
str2 = "人生苦短，我用Python"
# 三个单引号或者三个双引号可以输出一段
str3 = '''人生苦短，我用Python
你在说啥，我用PHP'''
str4 = """人生苦短，我用Python
你在说啥，我用PHP"""
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))

# 类型转换

# int()
print("int()函数")
n1 = 77.77
b1 = True
b2 = False
s1 = '77'
s2 = '77.77'
s3 = 'hello'
print(int(n1))  # 能转小数
print(int(b1))  # 能转布尔类型True
print(int(b2))  # 能转布尔类型False
print(int(s1))  # 能转整数字符串
"""
print(int(s2))  # 不能转小数字符串
print(int(s3))  # 不能转非数字字符串
"""

# float()
# 除了非数字字符串，关于数字的都能转，整数的转换后有小数部分.0
print("float()函数")
print(float(n1))
print(float(b1))
print(float(b2))
print(float(s1))
print(float(s2))
'print(float(s3)) # 不能转非数字字符串'

# str()
# 啥都能转
print("str()函数")
print(str(n1))
print(str(b1))
print(str(b2))
print(str(s1))
print(str(s2))
print(str(s3))
