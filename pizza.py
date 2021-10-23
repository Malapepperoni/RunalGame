def make_pizza(size,*toppings): #创建一个空的元组
    """打印顾客点的所有尺寸及配料"""
    print(f"\nMaking a {size}-inch pizza with the following topping: ")
    for topping in toppings:
        print(f"-{topping}")