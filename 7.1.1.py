promt = "If you tell us who you are,we can personalize the messages you see."
promt += "\nWhat is your first name? "
name = input(promt)
print(f"\nHello,{name.title()}")
ageint = "If you tell us how old you are,we can personalize the messages you see."
ageint += "\nWhat is your age? "
ageint = input(ageint)
print(f"\nI know your age,{ageint}!") #先打印 再紧接着使用int转换成数值
age = int(ageint)
if age >= 18:
    print(True)
else:
    print(False)



