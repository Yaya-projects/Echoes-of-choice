#Echoes of choice
import time
import random
credit = 0
user_name = input('Enter your name!:')
Weponary_loot = {'Mythril sword','Mythril wand','Mythril sword','Mythril wand','Gorgon Artifact'}
def choices_3 (option_a,option_b,option_c,scenario_a,scenario_b,scenario_c):
   while True:
      print(f'Now it is the time for you to make a descion {user_name}')
      print('Choose one of the following')
      print(f'A:{option_a}')
      print(f'B:{option_b}')
      print(f'C:{option_c}')
      choice = input('What have you chosen:').upper()
      if   choice == 'A':
         scenario_a()
         break
      elif choice == 'B':
         scenario_b()
         break
      elif choice == 'C': 
         scenario_c()
         break
      else:
         print('You have written an unaccepted value/letter please write one of the following a,b,c')
