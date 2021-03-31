#Make an empty list for storing aliens

aliens = []

#Make 30 green aliens

for alien_number in range(0,30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[3:16]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

#Show the first 5 aliens

for alien in aliens[:]:
    print(alien)

#Total number of aliens created

print('Total number of aliens that we have created are',len(aliens))