import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print("All friend put your card in bowl")

print("Random draw stared")

print(f"{random.choice(friends)} will pay the bill!")


#way 2 some long

setQuery = random.randint(0, len(friends)-1)

print(f"{friends[setQuery]} will pay the bill!")





