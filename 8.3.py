def get_formatted_name(first_name,last_name,middle_name=''):  #获取格式化了的名字
    """"返回整洁的名字,并判断名中名"""
    if middle_name:
        full_name = f"{first_name}{middle_name}{last_name}"
    else:
        full_name = f"{first_name}{last_name}"
    return full_name.title()

musician = get_formatted_name('xia','lang','mou')
#victorer = get_formatted_name('xia','lang')
#print(musician)
#print(victorer)

def get_bulid_name(first_name,last_name,age=None):  #获取格式化了的名字
    """返回设置好的名字,并含有年龄"""
    if age:
        person = {'first':first_name,'last':last_name,'age':age}
    else:
        person = {'first':first_name,'last':last_name}
    return person
person1 = get_bulid_name('xia','lang')
#person1 = get_bulid_name('xia','lang',22) #可以打印名字
print(person1)

while True:
    print("\nPlease tell me your name:")
    print("enter 'q or 0' at any time to quit")
    
    f_name = input("First_name: ")
    if f_name == 'q':
        break
    l_name = input("Last_name: ")
    if l_name == 'q':
        break
    y_age = input("you age: ")
    y_age = int(y_age)
    if y_age == 0:
        break
    bulid_name = get_bulid_name(f_name,l_name,y_age)
    print(f"\nHello!thank you {bulid_name['age']} years people, {bulid_name}!")
    #字典的调用[''] 
    ####将输入转化为数值
    ####y_age = input("you age: ")
    ####y_age = int(y_age)

