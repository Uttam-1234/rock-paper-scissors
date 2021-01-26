import random
lrock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

lpaper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

lscissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list=[lrock,lpaper,lscissors]
random_option = random.randint(0,2)
option_selected = input("Select 0 for stone,1 for paper,2 for scissor\n")
int_option_selected=int(option_selected)
if int_option_selected <= 2:
 print("you chose")
 print(list[int_option_selected])
 comp_option_selected = list[random_option]
 print("Computer chose")
 print(comp_option_selected)
 if int_option_selected==0 and random_option==0:
   print("Draw") 
 if int_option_selected==0 and random_option==1:
   print("You lose")
 if int_option_selected==0 and random_option==2:
   print("You win")
 if int_option_selected==1 and random_option==0:
   print("You win") 
 if int_option_selected==1 and random_option==1:
   print("Draw")
 if int_option_selected==1 and random_option==2:
   print("You lose")
 if int_option_selected==2 and random_option==0:
   print("You lose")
 if int_option_selected==2 and random_option==1:
   print("You win") 
 if int_option_selected==2 and random_option==2:
   print("Draw")
else:
  print("Invalid choice")