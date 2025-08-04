import random

choice = int(input("Rock:0, paper:1 or scissor:2?"))

options = random.randint(0,2)
print(options)
if choice==0 and options==2:
    print("You win!")

elif choice==1 and options==1:
    print("You win!")

elif choice==2 and options==1:
    print("You win!")

elif choice==options:
    print("Its a draw")
else:
    print("You lose")