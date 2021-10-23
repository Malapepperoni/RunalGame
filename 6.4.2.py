pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}

pizza2 = ('crust','thick','toppings',{
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
})

pizza3 = ('crust','thick','toppings',
 ['thick3', 'mushrooms3', 'extra cheese3' ] 
 )

pizza4 = ['crust','thick','toppings',
 {  'crust':'thick',
    'toppings':['mushrooms4','extra cheese4'],
 },
]


print(f"YOU ordered a {pizza['crust']}-crust pizza "
    "with the following toppings")

for topping in pizza['toppings']: #字典中嵌套列表
    print("\n" + topping) 

for toppinga in pizza2[3]['toppings']:  #元组中嵌套字典
    print("\n" + toppinga) 

for toppinga in pizza3[3]:    #元组中嵌套列表
    print("\n" + toppinga)     

for toppinga in pizza4[3]['toppings']:    #列表中嵌套字典
    print("\n" + toppinga)   


user = {
    'xialang':{
        'first':'xia',
        'last':'lang',
        'location':'liaoyang',
    },
    'chenyijia':{
        'first':'chen',
        'last':'yijia',
        'location':'yueqin',
    }
} 

for  username,user_info in user.items():
    print(f"Username:{username}")
    location1 = user_info['location']
    print(location1.title())    #字典嵌套字典 321

