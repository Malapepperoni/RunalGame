def get_users(names):
    """向#列表#中的每位用户发出简单的问候"""
    for name in names:
        massage = f"Hello,{name.title()}!"
        print(massage)

usernames = ['xl','cyj']
print(usernames)
#get_users(usernames[:])
get_users(usernames)
print(usernames)