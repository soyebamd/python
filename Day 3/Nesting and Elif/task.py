print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age=int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollercoaster")
    # price charges according to age below 16 - $5 between 16-18 - $8 18 and more = $10
    if age < 16:
        print("The ticket price is $5/ride")
    elif age < 18:
        print("The ticket price is $8/ride")
    else:
        print("The ticket price is $10/ride")
else:
    print("Sorry you have to grow taller before you can ride.")
