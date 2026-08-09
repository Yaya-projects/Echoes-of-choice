#Echoes of choice
import time
import random
score = 0
user_name = input('Enter your name!:')
Weponary_loot = {'Mythril sword','Mythril wand','Mythril sword','Mythril wand','Gorgon Artifact'}
v_rumour = {'Icey caves','Verdant forest'}
def slow_print(text,speed = 0.06):
   for charachter in text:
      print(charachter, end = "",flush = True)
      time.sleep(speed)
def score_update(added_score):
  global score 
  score =+ added_score
  if score >= 1:
    slow_print(f'Your current score is {score}!!',speed = 0.04) 
  else:
    slow_print(f'Your current score is {score}...',speed = 0.04)
def choices_3 (option_a,option_b,option_c):
    slow_print(f'Now it is the time for you to make a descion {user_name}\n')
    while True:
      slow_print(f'Choose one of the following\n')
      slow_print(f'A:{option_a}\n')
      slow_print(f'B:{option_b}\n')
      slow_print(f'C:{option_c}\n')
      global choice
      choice = input('What have you chosen:').upper()
      if choice in ['A','B','C']:
        break
      else:
       slow_print('You have written an unaccepted value/letter please write one of the following a,b,c\n',speed = 0.02)
def choices_2 (option_a,option_b):
    slow_print(f'Now it is the time for you to make a descion {user_name}\n')
    while True:
      slow_print(f'Choose one of the following\n')
      slow_print(f'A:{option_a}\n')
      slow_print(f'B:{option_b}\n')
      global choice
      choice = input('What have you chosen:').upper()
      if choice in ['A','B']:
        break
      else:
       slow_print('You have written an unaccepted value/letter please write one of the following a,b\n',speed = 0.02)
def choices_1 (option_a,):
    slow_print(f'Now it is the time for you to make a descion {user_name}\n')
    while True:
      slow_print(f'Choose one of the following\n')
      slow_print(f'A:{option_a}\n')
      global choice
      choice = input('What have you chosen:').upper()
      if choice in ['A','B']:
        break
      else:
       slow_print('You have written an unaccepted value/letter please write a since there are no other options left\n',speed = 0.02)













def start_game():
     global score
     score = 0
     slow_print(f'{user_name} wakes up to something licking them.\n {user_name} manages to shrug the thing off lightly.\n Once you open your eyes you realise that i was just your dog Buddy trying to wake you up.')
     slow_print(f'')