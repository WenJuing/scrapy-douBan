# 1）在列表里存储字典

gril_0 = {
    'name': '雷姆',
    'age': 15
}
gril_1 = {
    'name': '艾米莉亚',
    'age': 16
}
gril_2 = {
    'name': '碧翠丝',
    'age': 442
}
grils = [gril_0, gril_1, gril_2]

for g in grils:
    print(g)
# 使用循环生成多个字典组合
for i in range(10):
    new_gril = {'name': '御坂美琴', 'age': i}
    grils.append(new_gril)
print("输出前5个")
for g in grils[0:5]:
    print(g)

# 2）在字典里存储列表

skill = {
    'acfun': ['马赛克', '弹幕'],
    'bilibili': ['鬼畜', 'up主'],
    'cctv': ['国家频道', '电视台', '新闻']
}
for site, lable in skill.items():
    print(site, "的标签：")
    for la in lable:
        print(la)

# 3）在字典里存储字典

users = {
    'user_1': {
        'name': 'leimu',
        'age': 16
    },
    'user_2': {
        'name': 'lamu',
        'age': 17
    }
}
for user in users.values():
    print(user['name'], user['age'])
