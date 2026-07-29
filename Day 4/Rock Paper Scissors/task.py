import random
rock = '✊'

paper = '✋'

scissors = '✌️'


# Rules
# ✊ Rock beats Scissors
# Rock crushes Scissors.



# ✌️ Scissors beats Paper
# Scissors cuts Paper.


# ✋ Paper beats Rock
# Paper covers Rock.


#✊ vs ✊ → Draw 🤝

player = [rock, paper, scissors]

user_select = int(input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_select = random.choice(player)
#
# print(computer_select)
#
# print(player[user_select])

if player[user_select] == player[0] and computer_select == player[2]:
    print("✊ Rock beats Scissors")
    print(f"You chose {player[user_select]}")
    print(f"Computer Choose {computer_select}")
    print("You win!")

elif player[user_select] == player[2] and computer_select == player[1]:
    print("✌️ Scissors beats Paper")
    print(f"You chose {player[user_select]}")
    print(f"Computer Choose {computer_select}")
    print("You win!")




elif player[user_select] == player[1] and computer_select == player[0]:
    print("✋ Paper beats Rock")
    print(f"You chose {player[user_select]}")
    print(f"Computer Choose {computer_select}")
    print("You win!")


elif player[user_select] == computer_select:
    print(f"You choose{player[user_select]}")
    print(f"You chose {player[user_select]}")
    print("#✊ vs ✊ → Draw 🤝0")
    print(f"Computer Choose {computer_select}")


else:
    print(f"You choose{player[user_select]}")
    print("computer win")
    print(f"Computer Choose {computer_select}")


