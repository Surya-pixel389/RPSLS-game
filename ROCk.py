import random
print("=======================")
print("Rock, Paper and Scissor")
print("=======================")
print("Player choose:")
print("      1)✊")
print("      2)✋")
print("      3)✌️")
print("      4)🦎")
print("      5)🖖")

player = int(input("Players choice: "))
if player == 1:
    print("Your choice:✊")
elif player== 2:
    print("Your choice:✋")
elif player ==3:
    print("Your choice:✌️")
elif player == 4:
    print("Your choice:🦎")
elif player == 5:
    print("Your choice:🖖")
else:
    print("Wrong input")

comp = random.randint(1,5)
if comp <=1:
    print("Computer's choice:✊")
elif comp<=2:
    print("Computer's choice:✋")
elif comp<=3:
    print("Computer's choice:✌️")
elif comp<=4:
    print("Computer's choice:🦎")
else:
    print("Computer's choice:🖖")

if comp == player:
    print("Ties!!!!")
elif comp == 1 and  player ==3:
    print("Computer win")
elif comp == 2 and player == 1:
    print("Computer win")
elif comp ==3 and player ==2:
    print("Computer win")
elif comp == 1 and player == 4:
    print("Computer win")
elif comp ==  4 and player == 5:
    print("Computer win")
elif comp == 5 and player == 3:
    print("Computer win")
elif comp ==  3 and player == 4:
    print("Computer win")
elif comp == 4 and player ==2 :
    print("Computer win")
elif comp == 2 and player ==5:
    print("Computer win")
elif comp == 5 and player ==1:
    print("Computer win")
########
elif player == 2 or comp == 1:
    print("Player wins")
elif player == 3 or comp == 2:
    print("Player wins")
elif player == 1 or comp== 3:
    print("Player wins")
elif player ==1  or comp ==4 :
    print("Player wins")
elif player == 4 or comp ==5:
    print("Player wins")
elif player == 5 or comp ==3:
    print("Player wins")
elif player == 3 or comp ==4:
    print("Player wins")
elif player == 4 or comp ==2:
    print("Player wins")
elif player == 2 or comp ==5:
    print("Player wins")
elif player == 5 or comp ==1:
    print("Player wins")
else:
    print("error")
