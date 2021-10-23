def greet_uesr(UserName,UserLove='basketball'):#形参 只是个形式 且喜好的东西直接默认为篮球 
    """显示简单的问候语。"""
    print(f"Hello! {UserName.title()}!,Yeah!I konw you love {UserLove}.")
    
greet_uesr(UserLove='basketball',UserName='XiaLang')#实际的参数
#greet_uesr('XiaLang','basketball')#实际的参数
greet_uesr('cyj')
greet_uesr('cyj2',UserLove='xzq') #也可以直接修改默认值，将篮球改为薛之谦，Python解释器直接忽略篮球这个默认值