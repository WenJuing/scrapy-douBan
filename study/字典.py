user = {
    'name': 'leimu',
    'age': 16,
    'gender': '女'
}

# 遍历全部
for k, v in user.items():
    print('\nkey=', k)
    print('value=', v)
# 只遍历值
for v in user.values():
    print(v)

if 'leimu' in user.values():
    print("有")
else:
    print("没有")
if 'leimu' in user.keys():
    print("有")
else:
    print("没有")

# set()剔除重复值
user = {
    'aaa': 'C',
    'abk': 'Python',
    'ddd': 'JAVA',
    'nnn': 'C'
}
for v in user.values():
    print(v)
print('\n')
for v in set(user.values()):
    print(v)
