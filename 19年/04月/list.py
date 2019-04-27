aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
print(aliens.__len__())
for alien in aliens[:5]:
    print(alien)
print('......')
print('total number of aliens: ' + str(len(aliens)))
