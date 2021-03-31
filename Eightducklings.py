prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter != 'O' and letter != 'Q':
        print(letter + suffix)
    else:
        modify_suffix = 'uack'
        print(letter + modify_suffix)
