import random

user_wins = 0
computer_wins = 0
option = ("rock","paper","scissor")

while True:
    user_input = input("rock , paper , scissor or q for quit :").lower()
    if user_input == "q":
       break
    
    if user_input not in option:
     continue
    
random_number = random.randint(0,2)

computer_picks = option[random_number]
print("computrer picks : ",computer_picks + ".")

if user_input == "rock" and computer_picks == "scissor":
      print("you won!")
      user_wins +=1

elif user_input == "paper" and computer_picks == "rock":
    print("you won!")
    user_wins +=1

elif user_input == "scissor" and computer_picks == "paper":
      print("you won!")
      user_wins +=1
else :
    print("you lost try again")

print("user points :",user_wins )
print("computer points :",computer_wins)
  





