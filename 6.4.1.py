alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0, alien_1, alien_2] #alien 列表

#for alien in aliens:
#    print(alien)

alien_30 = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    alien_30.append(new_alien)

for alien in alien_30[:5]:
    if alien['color'] == 'green':
       alien['color']  = 'yellow'
       alien['prints'] = 10
       alien['speed']  = 'medium'
    elif alien['color'] == 'yellow':
       alien['color']  = 'red'
       alien['prints'] = 15
       alien['speed']  = 'fast'  

for alien in alien_30[:5]:
    print(alien)
print("……")

print(f"外星人数量是：{len(alien_30)}")