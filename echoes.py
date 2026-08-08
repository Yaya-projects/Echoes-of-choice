#Echoes of choice
import time
import random
credit = 0
user_name = input('Enter your name!:')
Weponary_loot = {'Mythril sword','Mythril wand','Mythril sword','Mythril wand','Gorgon Artifact'}
def slow_print(text,speed = 0.06):
   for charachter in text:
      print(charachter, end = "",flush = True)
      time.sleep(speed)
def choices_3 (option_a,option_b,option_c,scenario_a,scenario_b,scenario_c):
   while True:
      slow_print(f'Now it is the time for you to make a descion {user_name}\n')
      slow_print(f'Choose one of the following\n')
      slow_print(f'A:{option_a}\n')
      slow_print(f'B:{option_b}\n')
      slow_print(f'C:{option_c}\n')
      choice = input('What have you chosen:').upper()
      if   choice == 'A':
         if callable(scenario_a):
            scenario_a()
         else: 
          slow_print(f'{scenario_a}\n')
         break
      elif choice == 'B':
         if callable(scenario_b):
            scenario_b()
         else: 
            slow_print(f'{scenario_b}\n')
         break
      elif choice == 'C': 
         if callable(scenario_c):
            scenario_c()
         else: 
           slow_print(f'{scenario_c}\n')
         break
      else:
         slow_print('You have written an unaccepted value/letter please write one of the following a,b,c\n',speed = 0.02)

