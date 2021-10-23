import crm8_5 #原先只有做披萨的函数 故 导入整个模块
crm8_5.make_pizza(6,'pepperoni')
crm8_5.make_pizza(16,'mushrooms','green peppers','extra cheese')

from crm8_5 import make_pizza  #导入特定函数
make_pizza(6,'pepperoni')
make_pizza(16,'mushrooms','green peppers','extra cheese')

from crm8_5 import make_pizza as mp   #导入特定函数并指定别名
mp(6,'pepperoni')
mp(16,'mushrooms','green peppers','extra cheese')

from crm8_5 import *  #导入所有函数
get_users( ['xl','cyj'])

#引用的四种形式