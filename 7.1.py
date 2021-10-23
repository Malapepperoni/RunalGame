#7.2 //取整 
#使用while循环
number = 1
while number <= 5 : #先判断然后执行打印 再加1
    print(number)
    number += 1

active = True

while active:
    massage = input("please input some,expect quit!!!\n")

    if massage == 'quit':
        active = False
    else:
        print(massage)