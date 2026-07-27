print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("🏝️ ====================================")
print("🏴‍☠️  Welcome to Treasure Island!")
print("💰 Your mission is to find the treasure.")
print("🏝️ ====================================\n")

print("you\'are good human.")

# ------------------ First Choice ------------------
start_game = input("🛤️ Choose your path (Left ⬅️ / Right ➡️): ").lower().strip()

if start_game == "left":
    print("\n✅ Great choice! You safely reached the river.\n")

    # ------------------ Second Choice ------------------
    swim_or_wait = input("🌊 What will you do? Swim 🏊 or Wait ⏳: ").lower().strip()

    if swim_or_wait == "wait":
        print("\n⏳ You waited patiently.")
        print("🚤 A boat arrives and takes you across safely.\n")

        # ------------------ Third Choice ------------------
        door = input("🚪 Choose a door (🔴 Red / 🔵 Blue / 🟡 Yellow): ").lower().strip()

        if door == "red":
            print("\n🔥 You entered the Red Door.")
            print("🔥 Burned by fire!")
            print("💀 GAME OVER")

        elif door == "blue":
            print("\n🐺 You entered the Blue Door.")
            print("🐺 Eaten by a wild beast!")
            print("💀 GAME OVER")

        elif door == "yellow":
            print("\n💰 You entered the Yellow Door.")
            print("🎉 Congratulations!")
            print("🏆 YOU FOUND THE TREASURE!")
            print("👑 YOU WIN! 🎊")

        else:
            print("\n❌ That door doesn't exist.")
            print("💀 GAME OVER")

    elif swim_or_wait == "swim":
        print("\n🐊 You tried to swim.")
        print("🐊 Attacked by hungry crocodiles!")
        print("💀 GAME OVER")

    else:
        print("\n❌ Invalid choice.")
        print("💀 GAME OVER")

elif start_game == "right":
    print("\n🕳️ You fell into a deep hole.")
    print("💀 GAME OVER")

else:
    print("\n❌ Invalid path.")
    print("💀 GAME OVER")