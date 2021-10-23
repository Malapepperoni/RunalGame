def build_profile(first,last,**user_info):#### **创建一个空的元组
    """创建一个字典，其中包含我们知道的信息"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

#user_profile = build_profile('albert','einstein',location='princetion',field='physics')

#print(user_profile)
####运行结果{'location': 'princetion', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}