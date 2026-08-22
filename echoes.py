#Echoes of choice
import time
import random
def cap_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]
dog_bond = 25
score = 0
Weponary_loot = ['Mythril sword','Mythril wand','Mythril sword','Mythril wand','Gorgon Artifact']
v_rumour = {'Icey caves','Verdant forest'}
def slow_print(text,speed = 0.06):
   for charachter in text:
      print(charachter, end = "",flush = True)
      time.sleep(speed)
   print()
def bond_update(added_score):
  global dog_bond
  dog_bond += added_score
  if dog_bond >= 25:
    slow_print(f'Your current bond with {dog_name} is {dog_bond}!!',speed = 0.04) 
  else:
    slow_print(f'Your current score is {dog_bond}...',speed = 0.04)
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
      choice = input('What have you chosen:').upper()
      if choice in ['A','B','C','D']:
        return choice 
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
        return choice 
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
        return choice 
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
        return choice 
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
   slow_print(f'You yelp out in pain and once you regain your composure you glare at {dog_name}, who looks at you with innocent puppy eyes.')
   choices_2('Forgive her.','Scold her')
   if choice == 'A':
      slow_print('You scoff at her attempt to guilt trip you but you forgive her.')
      bond_update(5)
   else:
      slow_print('You scold her harshly and tell her to be more carefull next time because she did hurt you.')
      bond_update(-5)
   slow_print(f'After that, You chant the needed spell whilst holding the luminous shrooms and gravel in each of your hands.')
   slow_print(f'BAM! you and {dog_name} get blinded momentarly.\nAfter a few seconds both of you regain their vision.\nYou and {dog_name} find a luminous floating orb infront of you two.')
   slow_print(f'{dog_name}shakes her tail and starts barking esctatically whilst hopping around showing how proud she is of your achievement!!')
   slow_print(f'You pet her and give her a treat.\nYou start heading in deeper now with your magical light source.\nYou notice that there are bunch of lush on the stones and there are a variety of stones such as limestone!')
   slow_print(f'Every now and then you hear some slithering noises but you brush it off..\nYou head in deeper consequently the magical light you summoned`s effectivness diminishes as it is getting more darker.')
   slow_print(f'Whilst walking,you bump into something out of nowhere.\nYou feel a sharp pain in your head as you stumble backwards to the ground.\nIt takes you sometime to recover although you are slightly bleeding.\n{dog_name} returns with some healing leaves and more flint.\nTurns out that she went to find you some healing herbs that were on the rocks and more flint.')
   slow_print(f'{dog_name} looks like a mess all mudied up and dirty.\nYou hug her and start petting her.\n She starts licking your face.\nAfter the hug,you put one of healing herbs on your injury on your head.It`s gonna heal slowly but better than nothing!')
   slow_print(f'You start thinking of any applicable solution to increase the power of the mini light spirit')
   slow_print(f'You know? You should give him a name! It would be way easier than calling him mini light spirit..')
   while True:
    spirit_name = input('What are you gonna name the spirit!!?').strip()
    if spirit_name:
        break
    else:
        slow_print('Name cannot be empty. Please try again.')
   spirit_name = cap_first_letter(spirit_name)
   slow_print(f'Before you could think any further {spirit_name} starts hovering around the flint that {dog_name} had collected.')
   slow_print(f'You process what {spirit_name} is trying to convey.\nYou pick up the flints and hold {spirit_name} in each of your hands and chant once more.')
   slow_print(f'{spirit_name} starts glowing more brightly and they light up the cavern making it more clear.')
   slow_print(f'You look around for what you bumped into.It turns out to be sort of statue very niche.')    
   slow_print(f'Wait huh...?No it could not possibly be right...?\nThe statue..It was once a human too...\nIt`s head fell off from the impact with you and it`s bleeding..This isn`t safe....You need to go now.')
   slow_print(f'While you`re trying to escape frantically you and {dog_name}..\nYou realise you`re lost.. and can`t find the exit..You both continue runnig either way.')
   slow_print(f'You spot a place in the cave with some sunshine seeping through.You sprint over there along with {dog_name} and {spirit_name}')
   slow_print(f'You arrive there...but oh this isn`t any better there`s even more statues simillar to the previous ones...\nLooks like you made your way to that creatures lair.')
   slow_print(f'You start hearing some slithering and hisses')
   slow_print(f'Out of nowhere something lunges at you and pins you to the ground')
   slow_print(f'You closed you eyes just barely in time...You didn`t have enough time to witness the creature')
   choices_3(f'Call for {dog_name} to help you.',f'Grab a shard of stone from nearby and bash that things head..',f'Try to push it off')
   if choice == 'A':
    if dog_bond >= 30:
       slow_print(f'{dog_name} bites firmly on that things tail and injures it badly.')
       slow_print(f'It pulls away and you manage to carry {dog_name} and hide behind a statue to recollect yourself')
       bond_update(10)
       score_update(10)
    else:
       slow_print(f'{dog_name} reluctantly helps you by biting it just enough for it to back off for a few seconds')
       slow_print(f'You take this chance to hide behind one of the statues and you whisper to {dog_name} to follow you.\n You don`t make it that far tho.')
       bond_update(5) 
       score_update(6) 
   elif choice =='B':
      slow_print('You grunt as you try your hardest to reach out for a sharp stone nearby.\n You barely manage to grip it and then you start bashing the creature`s head multiple times.')  
      slow_print('Eventually it`s grip loosens and it backs off momentarly.') 
      slow_print(f'You take this chance to hide behind one of the statues and you whisper to {dog_name} to follow you.')
      slow_print(f'You and {dog_name} catch your breaths')
   else:
     if score > 7:
      slow_print(f'You manage to barely push that thing off your body.\nYou pull away barley.')
      slow_print(f'You scurry over behind a statue holding your breath while signing to {dog_name} to come here quietly')
      slow_print(f'{dog_name} crawls over to you and hides behind another statue close by..')
     else:
       if dog_bond >= 30:
        slow_print('You try to push it off but you fail miserably.')
        slow_print(f'Luckily {dog_name}  manages to throw some sand with her tail in that things eyes to blind it temporarly then drags you behind a statue nearby')
       else:
          slow_print(f'You try to push it off but you fail miserably.')
          slow_print(f'While trying to push it off, It bites you making you yelp in pain and open your eyes to meet it`s gaze...')
          slow_print(f'Before you could even react you notice that you can`t move your lower half...\nYou look down to see that your lower half has become stone..and whatever that thing did..\nIt appears that it`s like a disease it continues spreading around your body and right before it reaches your head\n.You shout at {dog_name} to run away')
          slow_print(f'{dog_name} starts running away and as he looks behind him one last time..He realises thay you have fully become stone..Like the surrounding statues...',0.07)
def Medusa_encounter():
   slow_print(f'You`re starting to panic and wondering what to do....\n {dog_name} looks at you with worried eyes..')
   choices_3(f'Attempt to communicate.',f'Search for any usable weapon.',f'Attempt to run away.')
   if choice == 'A':
      


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




def flowers_valley():
    slow_print(f'You start wandering around the terrain and collect flowers.\n A few minutes later,You`ve collected quite alot of flowers.\nYou look over to see what {dog_name} is doing..')
    slow_print(f'Turns out she has been collecting flowers alongside you!!') 
    choices_2(f'You thank her.',f'Compliment her')
    if  choice == 'A':
      slow_print(f'You take the flowers that she had collected, adding it to your collection and thank her for helping!')
      bond_update(2)
    else:
      slow_print('You add the flowers which she collected to your collection and take a pink flower and put it on her ear.')
      slow_print(f'You say: There! You look much more adorable like this {dog_name}')
      bond_update(5)
    slow_print('Both of you sit down amist the beautiful flowery terrain.\n You think about what to do next.')
def play_valley ():
   slow_print(f'You initiate a race with {dog_name} and the finish line is the tree over there!')
   slow_print('You count down 1...2...3 and the race begins!!')
   slow_print('Both of you start sprinting with all your might towards the tree.')
   slow_print(f'In the end,{dog_name} beat ya to it!!')
   slow_print('You start mumbling about how it was unfair.')
   slow_print(f'{dog_name} looks at you with a smug look.')
   slow_print(f'You look at her,noticing her smug expression, and you can`t help but laugh at her.')
   bond_update(10)
   slow_print('You rest under the tree a bit before deciding you should do something else.')  
def catch_valley ():
   slow_print(f'You take one of the twigs that fell down from the tree then throw it far.\n{dog_name} starts chasing it and brings it back.')
   slow_print(f'You repeat this for a few times before both of you start getting bored')
   bond_update(5)
def leave_valley():
   slow_print(f'You and {dog_name} start heading back to the location you woke up in.')
   slow_print(f'You arrive and you see the same structures you saw at the begining : The cave , The haunted mansion and the village.\n There`s also the valley but you already explored that')
   choices_3(f'Head to the haunted mansion.',f'Head to the cave',f'Head to the village.')
def Valley():
   slow_print(f'You traverse the valley along side with {dog_name}.')
   slow_print(f'After walking for a while, both of you arrive at a beautiful field filled with flowers and there`s a lone oak tree!!')
   choices_2(f'Collect some flowers.',f'Play with {dog_name} a bit.')
   if choice == 'A':
      flowers_valley()
   else:
      play_valley()
      choices_3(f'Play catch with {dog_name}.',f'Collect some flowers.',f'Go back to where you woke up.')
      if choice == 'A':
         catch_valley()
         choices_2(f'Collect some flowers.',f'Go back to where you woke up.')
         if choice == 'A':
            flowers_valley()
         else:
            leave_valley()
      elif choice == 'B':
         flowers_valley()
         choices_2(f'Play with {dog_name}.',f'Go back to where you woke up.')
         if choice == 'A':
            play_valley()
            choices_2(f'Play catch with {dog_name}.',f'Go back to where you woke up.')
            if choice == 'A':
              catch_valley()
              slow_print('You practically explored all of the valley.\nThere`s really nothing left to do.')
              slow_print('You decide to head back to where you came from.')
              leave_valley()
         else:
            leave_valley()
      else:
         leave_valley()




def start_game():
     global score
     global dog_bond
     score = 0
     dog_bond = 25
     global dog_name
     global user_name
     while True:
        user_name = input('What`s your name??:').strip()
        if user_name:
           break
        else:
           slow_print('Name cannot be empty. Please try again.')
     user_name = cap_first_letter(user_name) 
     slow_print(f'{user_name} wakes up to something licking them.\n you manage to shrug the thing off lightly.\n Once you open your eyes you realise that it was just your dog trying to wake you up.')
     while True:
        dog_name = input('Wait what was your dogs name again??(The dog is a female btw)').strip()
        if dog_name:
          break
        else:
           slow_print('Name cannot be empty. Please try again.')
     dog_name = cap_first_letter(dog_name)
     slow_print(f'You stand up and stretch lightly.\n You look around to find yourself under a tree in vast lush full valley.\n The valley is filled with a variety of flowers and plants!')
     slow_print(f'While walking along the valley with your beloved dog,You come across an ominous cave infront of you its entrance is a bunch of rocks that are covered with moss and vines...\n,as you look to your left far away theres an ominous haunted mansion it is emitting quite the astral aura...\n and on your right is the village you were brought up in!!\n or you could just hang out with {dog_name} in the valley a bit more!')
     slow_print(f'{dog_name} tilts her head and looks towards the cave.\nFor some reason you can sense that {dog_name} is nervous')
     choices_4(f'Enter the ominous cave.',f'Start heading towards the haunted mansion.',f'Head towards the village.',f'Spend some more time with {dog_name} in the valley.')