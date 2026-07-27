print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 175 and height <= 200:
    print("You are alright for this ride.")

elif height > 200:
    print("You are too high for this ride.")

else:
    print("Sorry, you are not alright for this ride.")