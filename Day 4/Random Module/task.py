import random
import mymodule
import triangle


print(random.random() * 10) #floating point number

print(random.randint(1, 10))    #int between a , b is parameter of randint function

mymodule.hello_user('Soyeb Ahmed')

print(random.uniform(1, 10))

#task print heads or tails with random number

#coins = [0,1]
#result = random.randint(coins[0], coins[1])

result = random.randint(0, 1)

if result == 0:
    print("You got heads")
else:
    print("You got tails")

#get all area of triangle
print("#get triangle")
print(triangle.triangle(60,60,100))

print("*" * 50)

print("#Find third angle")
#findthirdangle module
print(triangle.findthirdangle(60, 170))

