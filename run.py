import os


context = {'location': 'outside the house',
           'inventory': [],
           'weapons': [],
           'health': 100
           }


def get_help():
    print("""the available commands are: 
- map: shows you where you are on the map
- enter (followed by a location name): lets you enter a location
- take (followed by an item name): lets you take something into your possession
- context: shows you everything you need to know about yourself
- help: shows this menu""")

os.system('clear')
print('Welcome to the game')
get_help()
print('now go and save the world...')


def get_context(context):
    print('- you are', context['location'])
    print('- you have', get_inventory(context))
    print('- you have', get_weapons(context))
    print('- your health is at', get_health_status(context), '%')


def get_inventory(context):
    if context['inventory']:
        return context['inventory']
    else:
        return 'no inventory'


def get_weapons(context):
    if context['weapons']:
        return context['weapons']
    else:
        return 'no weapons'


def get_health_status(context):
    return context['health']


def map(current_location):
    print(f'you are currently standing {current_location}. there seems to be nothing around you apart from that')



while True:
    action = input('> ')
    if action == 'context':
        get_context(context)
    if action == 'map':
        map(context['location'])
    if action == 'help':
        get_help()



#
# class Room(object):
#
#     def enter(self, var):
#         # var = 101
#         print(f'{var}')
#
#
#     def look(self):
#         print('there not much to see here..')
#
#
#     def exit(self):
#         print('you have exited the room')
#
#
#
# class Monster(object):
#
#     def kill(self, use_weapon):
#         if use_weapon:
#             print('the beast is dead')
#         else:
#             print('you don\'t have a weapon. the beast killed you')
#
#
# class Dragon(Monster):
#
#     def scream(self):
#         print('i am a DRAGON! rarrrrrrr!')

