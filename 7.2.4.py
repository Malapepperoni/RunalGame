pormpt = "\nPlease enter the name of a city you have visited: "
pormpt +="\n(Enter 'quit' when you are finished.)"

while True:
    city = input(pormpt)
    if city == 'quit':
        break  #break 退出
    else:
        print(f"I'd love to go to{city.title()}!")

#打印奇数
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number %2 == 0:
        continue
    print(current_number)