#Echoes of choice
import time
import random
score = 0
user_name = input('Enter your name!:').capitalize()
Weponary_loot = ['Mythril sword','Mythril wand','Mythril sword','Mythril wand','Gorgon Artifact']
v_rumour = {'Icey caves','Verdant forest'}
def slow_print(text,speed = 0.06):
   for charachter in text:
      print(charachter, end = "",flush = True)
      time.sleep(speed)
   print()
def score_update(added_score):
  global score 
  score += added_score
  if score >= 1:
    slow_print(f'Your current score is {score}!!',speed = 0.04) 
  else:
    slow_print(f'Your current score is {score}...',speed = 0.04)
def choices_4 (option_a,option_b,option_c,option_d):
    slow_print(f'Now it is the time for you to make a descion {user_name}')
    while True:
      slow_print(f'Choose one of the following')
      slow_print(f'A:{option_a}')
      slow_print(f'B:{option_b}')
      slow_print(f'C:{option_c}')
      slow_print(f'D:{option_d}')
      global choice
      choice = input('What have you chosen:').upper()
      if choice in ['A','B','C','D']:
        break
      else:
       slow_print('You have written an unaccepted value/letter please write one of the following a,b,c,d',speed = 0.02)
def choices_3 (option_a,option_b,option_c):
    slow_print(f'Now it is the time for you to make a descion {user_name}\n')
    while True:
      slow_print(f'Choose one of the following')
      slow_print(f'A:{option_a}')
      slow_print(f'B:{option_b}')
      slow_print(f'C:{option_c}')
      global choice
      choice = input('What have you chosen:').upper()
      if choice in ['A','B','C']:
        break
      else:
       slow_print('You have written an unaccepted value/letter please write one of the following a,b,c',speed = 0.02)
def choices_2 (option_a,option_b):
    slow_print(f'Now it is the time for you to make a descion {user_name}')
    while True:
      slow_print(f'Choose one of the following')
      slow_print(f'A:{option_a}')
      slow_print(f'B:{option_b}')
      global choice
      choice = input('What have you chosen:').upper()
      if choice in ['A','B']:
        break
      else:
       slow_print('You have written an unaccepted value/letter please write one of the following a,b',speed = 0.02)
def choices_1 (option_a,):
    slow_print(f'Now it is the time for you to make a descion {user_name}')
    while True:
      slow_print(f'Choose one of the following')
      slow_print(f'A:{option_a}')
      global choice
      choice = input('What have you chosen:').upper()
      if choice in ['A']:
        break
      else:
       slow_print('You have written an unaccepted value/letter please write a since there are no other options left',speed = 0.02)
def Haunted_mansion ():
  slow_print(f'You arrive at the haunted mansion...')
  slow_print(f'You open the door gently...\nYou enter and a rush of cold wind runs past you.\nYou shiver a bit and look at {dog_name} to see that they are shivering too more than you are.')
  slow_print(f'The room is barely lit but enough just for you to be able to see just not as well compared to outside.')
  slow_print(f'As you walk around a bit and look around, you notice that the floor is not just wet but it feels like the floor is shifting with every step you take.\nThe texture of the floor and ceiling look a bit fleshy..')
  slow_print(f'While your are walking forward {dog_name} stumbles while walking due to the unnatural bending of the floor')
  slow_print(f'You stop as you realise you reached a crossed path.')
  slow_print(f'')



def start_game():
     global score
     score = 0
     global dog_name 
     slow_print(f'{user_name} wakes up to something licking them.\n you manage to shrug the thing off lightly.\n Once you open your eyes you realise that it was just your dog trying to wake you up.')
     dog_name = input('Wait what was your dogs name again??').capitalize()
     slow_print(f'You stand up and stretch lightly.\n You look around to find yourself under a tree in vast lush full valley.\n The valley is filled with a variety of flowers and plants!')
     slow_print(f'While walking along the valley with your beloved dog,You come across an ominous cave infront of you its entrance is a bunch of rocks that are covered with moss and vines...\n,as you look to your left far away theres an ominous haunted mansion it is emitting quite the astral aura...\n and on your right is the village you were brought up in!!\n or you could just hang out with {dog_name} in the valley a bit more!')
     slow_print(f'{dog_name} tilts their head and looks towards the cave.\nFor some reason you can sense that {dog_name} is nervous')
     choices_4(f'Enter the ominous cave.',f'Start heading towards the haunted mansion.',f'Head towards the village.',f'Spend some more time with {dog_name} in the valley.')