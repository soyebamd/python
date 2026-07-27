print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

bill = 0

if height >= 120 :

    age = int(input("What is your age? "))

    print("You can ride the rollercoaster")



    # price charges according to age below 16 - $5 between 16-18 - $8 18 and more = $10

    if age <= 16:

        bill = 5

        print("The ticket price is $5/ride")

    elif age <= 18:

        bill = 8

        print("The ticket price is $8/ride")

    elif age >=45 and age <= 55:

        print("The ticket is free for elder member")

    else:

        bill = 10

        print("The ticket price is $10/ride")

    #add addons of ride photo if user want

    photo_price = 3

    add_photo = input(f"Do you want a ride photo for ${photo_price}? y or n? ").lower()

    if add_photo == "y":

        photo_price = 3

        bill += photo_price

        print("Photo added, The ride price is $3/ride")

    else:

        photo_price = 0

        print("Photo not added to ride price")

    print(f"The total ###ticket price is ${bill}")

else:

    print("Sorry you have to grow taller before you can ride.")

