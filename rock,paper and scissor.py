#   This is rock,paper and scissor game

name = input("Enter Your Name:")
print("Hello", name )

# so anyone cant enter other char
while True:
 choice = input("Choose r(rock)/p(paper)/s(scissor):")
 if choice not in ["r","p","s"]:
   print("Invalide")
   continue
 else:
  # print("your choice is ",choice)
  break
 
# pc will choose randomly
import random
choices = ["r", "p", "s"]
computer_choice = random.choice(choices)

#conditions of win,lose and tie 
if choice == computer_choice:
  print("Tie")

elif choice == "r" and computer_choice == "s":
  print("You Win")
elif choice == "s" and computer_choice == "p":
  print("You Win")
elif choice == "p" and computer_choice == "r":
  print("You Win")

else:
  print("You Lose")

# in last it will show what you and computer choose
print("your choice is ",choice)
print("Computer choice is ",computer_choice)


