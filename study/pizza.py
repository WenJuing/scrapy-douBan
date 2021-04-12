def make_pizza(size, *material):    # 提示：*代表生成一个空元组
    '''打印这个披萨的所有原料'''
    print("\nMaking a " + size + " pizza with the following material:")
    for m in material:
        print("-", m)
