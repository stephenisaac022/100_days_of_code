print('''
      WELCOME TO TREASURE ISLAND 
       _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
YOUR MISSION IS TO FIND THE MISSING TREASURE WHETHER DEAD OR ALIVE 
   🏴‍☠️  🏴‍☠️  🏴‍☠️  🏴‍☠️  🏴‍☠️  🏴‍☠️  🏴‍☠️  🏴‍☠️  🏴‍☠️''')
print('WELCOME TO TREASURE ISALAND PRESS .......STILL LOADING ....🐫🦙🦡🦥🪙🏝️🏴‍☠️ ')
print('YOUR  MISSION IS TO FIND THE TREASURE.')
ist_choice = input('Do you want to go left or right \n ').lower()
if ist_choice == 'left':
   second_choice = input('you came near a river you have to wait or swim \n ').lower()
   if second_choice == 'Swim':
      third_choice = input('''you have waited....a boat came and carry you..
                            you are before 2 door which one do you want follow
                             RED or BLUE''').lower()
      if third_choice == 'red' or third_choice == 'blue' :
        print ('GAME OVER LOL......RBY😁')
      elif third_choice == 'yellow' :
        print('''you are a genius you have found the TREASURE 💫💫🥇...YOU
                                  YOU ROCK''')
      else :
        print('GAME OVER...YOU ARE A FAILURE...LOL')
        
   else :
      print ('oooh..no you got attack by a trout..GAME OVER.')
      
else :
   print('ooops, You Fell into a hole ')