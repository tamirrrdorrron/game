import os
from sys import exit


os.system('clear')
print("""Welcome to the game""")

player_name = input('please enter your name: ')

print(f'ok, {player_name}, let\'s play')
print('the available commands are: map, enter (followed by a room name), take (followed by an item)')
print('now go and save the world...')

current_location = 'outside the house'
action = input('> ')


def map(current_location):
    print(f'you are currently standing {current_location}. there seems to be nothing around you apart from that')


if action == 'map':
    map(current_location)
else:
    exit(0)

action = input('> ')

if action == 'enter house':
    print('you have entered the house. there are a few rooms in the house.')
