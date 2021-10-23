def make_pizza(size,*toppings): #创建一个空的元组
    """打印顾客点的所有尺寸及配料"""
    print(f"\nMaking a {size}-inch pizza with the following topping: ")
    for topping in toppings:
        print(f"-{topping}")

def get_users(names):
    """向#列表#中的每位用户发出简单的问候"""
    for name in names:
        massage = f"Hello,{name.title()}!"
        print(massage)

#make_pizza(5,'pepperoni')
#make_pizza(16,'mushrooms','green peppers','extra cheese')
####运行结果
####Making a 5-inch pizza with the following topping:
####-pepperoni
####
####Making a 16-inch pizza with the following topping:
####-mushrooms
####-green peppers
####-extra cheese

