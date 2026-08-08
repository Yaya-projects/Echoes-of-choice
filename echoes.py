#Echoes of choice
import random
credit = 0
user_name = input('Enter your name!:')
Weponary_loot = {'Mythril sword','Mythril wand','Mythril sword','Mythril wand','Gorgon Artifact'}
option_a = ''
option_b = ''
option_c = ''
def choices_3 (option_a,option_b,option_c):
    print(f'Now it is the time for you to make a descion {user_name}')
    print('Choose one of the following')
    print(f'A:{option_a}')
    print(f'B:{option_b}')
    print(f'C:{option_c}')
    global choice 
    choice = input('What have you chosen:').upper()
choices_3(option_a = 'Cross the bridge',option_b ='find a short cut',option_c = 'idk man')
if choice == 'A':
   print('....')
elif choice == 'B':
   print('...')
elif choice == 'C':
   print('....')
else:
    print ('ew')

