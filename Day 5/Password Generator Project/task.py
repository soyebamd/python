import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#print(letter_range)

random_password = []

for letter in range(0, nr_letters ):
    #print(random.choice(letters))
    random_password.append(random.choice(letters))


for number in range(0, nr_numbers ):
    #print(random.choice(numbers))

    random_password.append(random.choice(numbers))


for symbol in range(0, nr_symbols ):
    #print(random.choice(symbols))

    random_password.append(random.choice(symbols))

print("simple version password length is:", len(random_password))
print("".join(random_password))

#Hard Version
#When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:
#x$d24g*f9

print ("version 2 complex password")
#
# print(random_password)

hard_version_password = random.sample(random_password, len(random_password))

get_final_version_password = "".join(hard_version_password)

print(f"Hard Version Password: {get_final_version_password} ")


#how to concat string , nums simply

#random word

random_word = ""

for i in range(0, 10):

    random_word += random.choice(letters)
    print(f"Random Word: {random_word}")

print("random word is:", random_word)









