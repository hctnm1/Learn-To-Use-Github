#This is all about the Rock Paper Scissors Game using simple if,elif and else statements
#initializing a symbol for rock, paper and scissors to make it vizualize better
#at places i have added emojis like this (\U0001F44A) to make it much more interesting 
#u can run this code in any python ide compiler
   
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Let's get back to our childhood days through this game!!.")
import random
gamer=int(input("What do u choose? Type 0 for rock,1 for paper, 2 for scissor: "))
if(gamer==0):
  print(rock, "\U0001F44A")
elif(gamer==1):
  print(paper,"\U0001f590")
elif(gamer==2):
  print(scissors,"\U0001f91e")   
else:
  print("it's completely out of the options available,ur not allowed:-(")
print("Computer Chooses: ")
random_chose=random.randint(0,2)
print(random_chose)
if(random_chose==0):
  print(rock,"\U0001F44A")
elif(random_chose==1):
  print(paper,"\U0001f590")
elif(random_chose==2):
  print(scissors,"\U0001f91e")  
if (gamer) >3 or (gamer) < 0: 
  print("You typed an invalid number, you lose!") 
elif (gamer) == 0 and (random_chose)== 2:
   print("You win!")
elif (random_chose) == 0 and (gamer)== 2:
   print("You lose")
elif (random_chose) > (gamer):
  print("You lose")
elif (gamer) > (random_chose):
 print("You win!")
elif (gamer) == (random_chose):
  print("It's a draw")
print("Happy Coding Cheers !!!!")    
