import sys
from random import randint


hp = 100
print('Welcome to the Terminal Adventure!')
print('This is an attempt at a small RPG with choice options. Lets begin!')

# Q1

print('You are walking through the jungle.\n'
'You hear rustling leafs and all of a sudden a gigantic gorilla drops infront of your feet.')
print('You identify 2 options: try to distract the gorilla or you try to rush past him.')
q1 = int(input('What option do you pick? 1 or 2: '))
if q1 == 1:
    print('You pick up a stick and throw it against a tree.')
    dmg = randint(10, 30)
    hp = hp - dmg
    print(f'The gorilla doesn\'t seem impressed and throws a stick of his own - at your head.\n'
          f'The stick scraped your neck, and you took {dmg} damage.\n'
          f'You assess your condition, and find out you only have {hp} hp left! ')
else:
    print('You make a run for it. The gorilla catches your movement out of the corner of his eye.')
    dmg = 100
    hp = hp - dmg
    print(f'Just as you make it past the gorilla, you feel something grab your foot and you fall flat on the ground.\n' \
    f'The gorilla grabs you by the ankles and starts smashing you into the ground.\n'
    f'It breaks all your bones and you have {hp} hp left!\n'
    'GAME OVER!')
    sys.exit()

# Q2

print('You\'ve managed to make it past the gorilla. You have been worn out and feel thirsty.\n'
'You continue walking and find a small river. Something feels off, but the thirst is massive.\n'
'You think about either drinking directly from the river or to look for another source of water.')
q2 = int(input('What will you do? 1 of 2? '))
if q2 == 1:
    dmg = 100
    hp = hp - dmg
    print('You decide to drink from the river.\n'
    'You get on your knees to drink, and before you know it, a crocodile jumps out of the water.\n' \
    f'He pulls you under and you drown, leaving you at {hp} hp.\n'
    'GAME OVER!')
    sys.exit()   
else:  
    print('You walk along the river bank, and eventually find a small stream of water coming down.\n'
          'You decide to drink directly from the stream. That\'s better!')
    dmg = randint(10,20)
    hp = hp - dmg
    print('After you continue to walk, you start to feel a bit ill. The water must have contained something.\n' \
    'You lie down and fall asleep. When you wake up you feel weak.\n' 
    f'The water was poisoned, and you find out you only have {hp} hp left...\n'
    'Atleast youre still kicking! You continue your adventure.')

# Q3

print('You\'ve been walking all day, and feel tired.\n' 
'You need a place to sleep. You have two options:')
q3 = int(input('Will you seek shelter in the cave you walked past a few minutes ago?\n' 
'Or do you climb high up in a tree? 1 or 2? '))
if q3 == 1:
    print('You go back to the cave, grab some dead wood and light a fire.' 
    'You fall asleep next to the warm fire.')
    dmg = randint(10,20)
    hp = hp - dmg
    print('You wake up and find you have been bitten by a rattlesnake that was attracted by the fire\n' \
    f'You have taken {dmg} damage and only have {hp} hp left...')
else:
    print('You fall asleep. You wake up and find a monkey took your shoes!')
    dmg = 5
    hp = hp - dmg
    print('It hurts a bit to climb in the tree, and you get some blisters.\n' \
    f'You take a little damage and have {hp} left.')

# Q4

print('The sun rises while you want to get moving again. \n' \
'All of a sudden, in the distance, you hear a faint sound of chopper blades.\n'
'You know this is your only shot to be saved.\n' \
'Do you get up high in a tree? Or do you try to make smoke signals with a fire?')
q4 = int(input('What do you pick? 1 or 2? '))
if q4 == 1:
    print('You decide to get as high as possible to get the pilots attention.\n' \
    'You are almost at the top, when a branch breaks. You fall all the way down... Unfortunate.\n'
    'GAME OVER!')
else:
    print('You (re)light the fire and use your shirt to make signals...\n' \
    'S..O..S...\n' \
    'S...O...S...\n' \
    'S.....O......S....\n' \
    'There doesn\'t seem to be any response. You are drowsing off and eventually fall asleep.')
    print('The fire went out while you were asleep, and you froze to death. Unfortunate.\n'
          'GAME OVER!')

print('Thank you for playing! There are no winners in this game. No one could surive the jungle, don\'t worry ;-)')