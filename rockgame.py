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

user_input = int(input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_select = random.randint(0, 2)
# print(user_input)
# print(computer_select)

print(f"You chose {player[user_input]}")
print(f"Computer Choose {player[computer_select]}")


if user_input > len(player)-1:
    print("Now allowed")

elif user_input > computer_select:

    print(f"You Win")


elif user_input < computer_select:

    print(f"You Loss")

elif user_input == computer_select:
    print("Draw")

else:
    print(f"noting")




#
# print(player[user_select])

#
# print(computer_select > user_select)

#
# #
# if user_select > computer_select:
#     print(f"You chose {user_select}")
#     print(f"Computer Choose {computer_select}")
#     print("You win!")
#
# elif user_select == computer_select:
#     print(f"You chose {user_select}")
#     print(f"Computer Choose {computer_select}")
#     print(f"#{user_select} vs {computer_select} → Draw 🤝")
#
# else:
#     print(f"You choose{user_select}")
#     print("computer win")
#     print(f"Computer Choose {computer_select}")
