favorite_language = { #是某些人喜好某语言的一个字典
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

friends = ['phil','sarah']#是关于好朋友的列表
for name in favorite_language.keys():#仅取键值
    print(f"Hi {name.title()}")
    if name in friends:
       language = favorite_language[name].title()#新定义一个变量 等于favorite_language中键所对应的值并大写首字母
       print(f"\t{name.title()},I see you love {language}!") #缩进\t

print(favorite_language)#遍历字典

print(favorite_language.keys())#遍历字典中的键

print(favorite_language.values())#遍历字典中的键值

print(set(favorite_language.values()))#遍历字典中的键值,同时剔除重复项