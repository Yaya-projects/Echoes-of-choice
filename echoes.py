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
def Medusas_Cave():
   slow_print(f'You muster up the courage to enter the cave!!')
   slow_print(f'While you are making your way in you,you start taking a look at the insides of this cave or now rather cavern?')
   slow_print(f'You cannot really make out the insides since there is literally no light..\nLucky for you there are some luminous shrooms around.')
   slow_print(f'You recall from one of your classes at school related to support magic back in the village.\nThat if you chant a spell with some luminous shrooms and some gravel you can make a mini light spirit!')
   slow_print(f'I`ve got the shrooms now what about the gravel.....?')
   slow_print(f'Not even a second later after you`ve muttered that to yourself, {dog_name} jumps on you excitedly with a bunch of gravel stones in her mouth with a silly grin.\n You are understandablly baffled but laugh at how she looks with all those gravels in her mouth looking like a chipmunk.')
   slow_print(f'{dog_name} spits all the gravels on the ground so you can pick them up then spits one at you for laughing at them.')
   slow_print(f'You yelp out in pain and once you regain your composure you glare at {dog_name}, who looks at you with innocent puppy eyes.\nYou scoff at ther attempt to guilt trip you but you forgive her.')
   slow_print(f'You chant the needed spell whilst holding the luminous shrooms and gravel in each of your hands.')
   slow_print(f'BAM! you and {dog_name} get blinded momentarly.\nAfter a few seconds both of you regain their vision.\nYou and {dog_name} find a luminous floating orb infront of you two.')
   slow_print(f'{dog_name}shakes her tail and starts barking esctatically whilst hopping around showing how proud she is of your achievement!!')
   slow_print(f'You pet her and give her a treat.\nYou start heading in deeper now with your magical light source.\nYou notice that there are bunch of lush on the stones and there are a variety of stones such as limestone!')
   slow_print(f'Every now and then you hear some slithering noises but you brush it off..\nYou head in deeper consequently the magical light you summoned`s effectivness diminishes as it is getting more darker.')
   slow_print(f'Whilst walking,you bump into something out of nowhere.\nYou feel a sharp pain in your head as you stumble backwards to the ground.\nIt takes you sometime to recover although you are slightly bleeding.\n{dog_name} returns with some healing leaves and more flint.\nTurns out that she went to find you some healing herbs that were on the rocks and more flint.')
   slow_print(f'{dog_name} looks like a mess all mudied up and dirty.\nYou hug her and start petting her.\n She starts licking your face.\nAfter the hug,you put one of healing herbs on your injury on your head.It`s gonna heal slowly but better than nothing!')
   slow_print(f'You start thinking of any applicable solution to increase the power of the mini light spirit')
   slow_print(f'You know?You should give him a name!It would be way easier than calling him mini light spirit..')
   spirit_name = input('What are you gonna name the spirit!!?').capitalize()

slow_print(f'{user_name}')

def Haunted_mansion ():
  slow_print(f'You arrive at the haunted mansion...')
  slow_print(f'You open the door gently...\nWhile entering, a rush of cold wind greets you.\nYou shiver a bit in response then look at {dog_name} to see that she is shivering way more than you are.')
  slow_print(f'The room is barely lit but enough for you to be able to make out the surrounding just not see as well compared to outside.')
  slow_print(f'As you walk a bit and look around, you notice that the floor is not just wet but it feels like the floor is shifting with every step you take.\nThe texture of the floor and ceiling look a bit fleshy..')
  slow_print(f'While your are walking forward {dog_name} stumbles while walking due to the unnatural bending of the floor')
  slow_print(f'You cant help but start giggling to yourself but your attempt to hide it is futile and {dog_name} still catches you.\n {dog_name} side eyes you and lets out a bark simillar to a pout.')
  slow_print(f'You pet him as a form of apology.\nYou and {dog_name} continue walking for what seems like hours.')
  slow_print(f'You arrive at some sort of lobby or living room??')
  slow_print(f'You decide to rest up and take a break in this room as you look around you realise that the lobby leads into 3 diffrent paths.')
  slow_print(f'The first being is that you continue walking down the hallway straight but you can hear faint whispers.\nYou reach your hand out and the air is so suffocating to the point you can feel the diffrence simply from your hand.')
  slow_print(f'The second is a room on the right with its door closed... but you can hear some rumbling accompanied by some low growls.')
  slow_print(f'The third is also a room smillar to the previous one but on the left and the obvious of a missing door and a pile of dust where it should be...')
  choices_3 (f'Enter the room on the right?',f'Continue walking forward in the hallway?',f'Enter the doorless room on the left?')
def Haunt_Man_Left():
    slow_print(f'You open the door slowly and cautiously and tell {dog_name} to stay outside.')
    slow_print(f'The texture of the floor remains consistent even in this room but you cannot shake of the feeling that your being watched or stared at....')
    slow_print(f'')#continue after you finish the gorgon cave and the dogs evolution system.

def start_game():
     global score
     score = 0
     global dog_name 
     slow_print(f'{user_name} wakes up to something licking them.\n you manage to shrug the thing off lightly.\n Once you open your eyes you realise that it was just your dog trying to wake you up.')
     dog_name = input('Wait what was your dogs name again??(The dog is a female)').capitalize()
     slow_print(f'You stand up and stretch lightly.\n You look around to find yourself under a tree in vast lush full valley.\n The valley is filled with a variety of flowers and plants!')
     slow_print(f'While walking along the valley with your beloved dog,You come across an ominous cave infront of you its entrance is a bunch of rocks that are covered with moss and vines...\n,as you look to your left far away theres an ominous haunted mansion it is emitting quite the astral aura...\n and on your right is the village you were brought up in!!\n or you could just hang out with {dog_name} in the valley a bit more!')
     slow_print(f'{dog_name} tilts her head and looks towards the cave.\nFor some reason you can sense that {dog_name} is nervous')
     choices_4(f'Enter the ominous cave.',f'Start heading towards the haunted mansion.',f'Head towards the village.',f'Spend some more time with {dog_name} in the valley.')