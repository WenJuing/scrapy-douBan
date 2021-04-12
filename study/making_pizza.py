""" # 导入整个模块
import pizza as p   # 通过as给模块起个别名


p.make_pizza('biggest', 'beet', 'meat')
 """

# 导入特定函数
from pizza import make_pizza as mp  # 通过as给函数起个别名


mp('smallest', 'noodle', 'vegetable')
