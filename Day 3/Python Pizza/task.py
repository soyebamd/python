print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#What size pizza do you want? S, M or L: L

bill = 0

if size == "S":
    bill += 15
    print("Small pizza (S): $15")


elif size == "M":
    bill += 20


elif size == "L":
    bill += 25
    print("Large pizza (L): $25")




else:
    print("No order.")

if pepperoni == "Y":
    if size == "S":
        bill += 2
        print(f"pepperoni added (M): $2")

    else:
        bill += 3
        print(f"pepperoni added (L): $3")



if extra_cheese == "Y":
    bill += 1
    print("Extra cheese added: $1")

if bill >0:
    print(f"Your final bill is: ${bill}")
