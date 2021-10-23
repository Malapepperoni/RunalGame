unconfirmed_users =  ['alice','brian','candace']
confirmed_users =  []

while unconfirmed_users:
    current_user = unconfirmed_users.pop() #从末尾弹出一个量

    print(f"Verifying user:{current_user.title()}")
    confirmed_users.append(current_user) #往列表间添加 

print("\nThe following user have been confirmed: ")

for confirmed_user in confirmed_users:
    print (confirmed_user.title())

while 'alice' in confirmed_users:
    confirmed_users.remove('alice')

for confirmed_user in confirmed_users:
    print (f"\n{confirmed_user.title()}")   #.3.2 删除特定元素
